#!/usr/bin/env python3
import json
import os
import re
from html import unescape
from urllib.parse import quote

import requests
from util import ROOT, load_config, load_env, notion_headers

_cfg = load_config()
SEARCH_CFG = _cfg["linkedin"]["search"]
TARGET_ROLES = _cfg["linkedin"]["filters"]["target_roles"]
TARGET_SENIORITY = _cfg["linkedin"]["filters"]["target_seniority"]


def query_all_rows(db_id, h):
    out, cur = [], None
    while True:
        payload = {"page_size": 100}
        if cur:
            payload["start_cursor"] = cur
        r = requests.post(f"https://api.notion.com/v1/databases/{db_id}/query", headers=h, data=json.dumps(payload), timeout=30).json()
        out.extend(r.get("results", []))
        if not r.get("has_more"):
            break
        cur = r.get("next_cursor")
    return out


def rich(prop):
    return "".join(x.get("plain_text", "") for x in prop.get("rich_text", [])).strip()


def ensure_column(db_id, name, col_type, h):
    db = requests.get(f"https://api.notion.com/v1/databases/{db_id}", headers=h, timeout=30).json()
    props = db.get("properties", {})
    if name in props and props[name].get("type") == col_type:
        return
    requests.patch(
        f"https://api.notion.com/v1/databases/{db_id}",
        headers=h,
        data=json.dumps({"properties": {name: {col_type: {}}}}),
        timeout=30,
    )


def existing_job_ids(db_id, h):
    ids = set()
    for row in query_all_rows(db_id, h):
        val = rich(row.get("properties", {}).get("job_id", {}))
        if val:
            ids.add(val)
    return ids


def parse_job_cards(html):
    jobs = []
    for m in re.finditer(r"<li>(.*?)</li>", html, re.S):
        s = m.group(1)
        idm = re.search(r"jobPosting:(\d+)", s)
        hrefm = re.search(r'href="([^"]*linkedin\.com/jobs/view/[^"]+)"', s)
        titlem = re.search(r"<h3[^>]*>\s*(.*?)\s*</h3>", s, re.S)
        compm = re.search(r'job-search-card-subtitle"[^>]*>\s*(.*?)\s*</a>', s, re.S)
        if not (idm and hrefm and titlem and compm):
            continue
        jobs.append({
            "id": idm.group(1),
            "url": unescape(hrefm.group(1)).replace("&amp;", "&"),
            "position": re.sub(r"<[^>]+>", "", unescape(titlem.group(1))).strip(),
            "company": re.sub(r"<[^>]+>", "", unescape(compm.group(1))).strip(),
        })
    return jobs


def extract_jd_text(job_html):
    # Strictly extract JD body only; if missing, return empty so caller can mark parsing issue.
    m = re.search(r'<div class="show-more-less-html__markup[^>]*>([\s\S]*?)</div>', job_html)
    if not m:
        return ""
    txt = m.group(1)
    txt = re.sub(r"<script[\s\S]*?</script>", "", txt)
    txt = re.sub(r"<style[\s\S]*?</style>", "", txt)
    txt = txt.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
    txt = re.sub(r"</p>", "\n\n", txt)
    txt = re.sub(r"</li>", "\n", txt)
    txt = re.sub(r"<[^>]+>", "", txt)
    txt = unescape(txt)
    lines = [ln.strip() for ln in txt.splitlines()]
    # remove common non-JD metadata noise
    noisy = []
    for ln in lines:
        l = ln.lower()
        if not ln:
            noisy.append("")
            continue
        if re.search(r"\b\d+[+,]?\s+applicants?\b", l):
            continue
        if re.search(r"\b(posted|reposted|\d+\s+(day|days|hour|hours|week|weeks)\s+ago)\b", l):
            continue
        if l in {"about the job", "job description"}:
            continue
        noisy.append(ln)
    txt = "\n".join(noisy)
    txt = re.sub(r"\n{3,}", "\n\n", txt).strip()
    if len(txt) > 18000:
        txt = txt[:18000] + "\n\n[Truncated]"
    return txt


def jd_to_children(jd_text):
    if not jd_text.strip():
        return []
    chunks = []
    for para in [p.strip() for p in jd_text.split("\n\n") if p.strip()]:
        while len(para) > 1800:
            chunks.append(para[:1800])
            para = para[1800:]
        chunks.append(para)
    return [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {"rich_text": [{"type": "text", "text": {"content": c}}]},
        }
        for c in chunks[:80]
    ]


def reject_reason(jd, position):
    txt = (jd + "\n" + position).lower()
    if re.search(r"\b([8-9]|\d{2,})\+?\s*years?\b", txt):
        return "exp_8plus"
    pos_lower = position.lower()
    if not any(x in pos_lower for x in TARGET_ROLES):
        return "non_target_role"
    if not any(x in pos_lower for x in TARGET_SENIORITY):
        return "non_target_seniority"
    return None


def run(env_path=None):
    if env_path is None:
        env_path = str(ROOT / ".env")
    load_env(env_path)
    token = os.environ["NOTION_TOKEN"]
    db_id = os.environ["DB_ID"]
    if "-" not in db_id and len(db_id) == 32:
        db_id = f"{db_id[:8]}-{db_id[8:12]}-{db_id[12:16]}-{db_id[16:20]}-{db_id[20:]}"

    h = notion_headers(token)
    ensure_column(db_id, "note", "rich_text", h)
    ensure_column(db_id, "job_id", "rich_text", h)

    summary = {
        "searched": 0, "accepted": 0, "rejected": 0,
        "rejected_by_reason": {"exp_8plus": 0, "non_target_role": 0, "non_target_seniority": 0},
        "added": 0, "skipped": 0,
    }

    # LinkedIn search + strict reject (deterministic)
    seen = set()
    accepted_jobs = []
    roles = [f"{s} {r}" for s in TARGET_SENIORITY for r in TARGET_ROLES]
    for r in roles:
        start = 0
        while True:
            url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={quote(r)}&location={SEARCH_CFG['location']}&f_TPR={SEARCH_CFG['f_tpr']}&sortBy={SEARCH_CFG['sort_by']}&start={start}"
            html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=25).text
            cards = parse_job_cards(html)
            if not cards:
                break
            summary["searched"] += len(cards)
            for j in cards:
                if j["id"] in seen:
                    continue
                seen.add(j["id"])
                jd_html = requests.get(f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{j['id']}", headers={"User-Agent": "Mozilla/5.0"}, timeout=25).text
                reason = reject_reason(jd_html, j["position"])
                if reason:
                    summary["rejected"] += 1
                    summary["rejected_by_reason"][reason] = summary["rejected_by_reason"].get(reason, 0) + 1
                    continue
                j["jd_text"] = extract_jd_text(jd_html)
                accepted_jobs.append(j)
                summary["accepted"] += 1
            start += 25

    # skip jobs already in notion (idempotent via linkedin job id)
    notion_ids = existing_job_ids(db_id, h)
    new_jobs = [j for j in accepted_jobs if j["id"] not in notion_ids]
    summary["skipped"] = len(accepted_jobs) - len(new_jobs)

    # insert accepted jobs to notion
    for j in new_jobs:
        payload = {
            "parent": {"database_id": db_id},
            "properties": {
                "Name": {"title": [{"type": "text", "text": {"content": j["company"][:200]}}]},
                "URL": {"url": j["url"]},
                "position": {"rich_text": [{"type": "text", "text": {"content": j["position"][:2000]}}]},
                "job_id": {"rich_text": [{"type": "text", "text": {"content": j["id"]}}]},
                "Status": {"status": {"name": "Not started"}},
                "note": {"rich_text": [{"type": "text", "text": {"content": "accepted by strict filters"}}]}
            },
            "children": jd_to_children(j.get("jd_text", ""))
        }
        r = requests.post("https://api.notion.com/v1/pages", headers=h, data=json.dumps(payload), timeout=30).json()
        if r.get("object") == "page":
            summary["added"] += 1
        else:
            print(f"[NOTION INSERT FAIL] {j['company']} — {j['position']}", flush=True)
            print(f"  response: {json.dumps(r, ensure_ascii=False)}", flush=True)

    # scope of this script: LinkedIn search/filter + Notion insert + JD content retention only
    summary["script_scope"] = "linkedin_to_notion_jd_only"
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    run()
