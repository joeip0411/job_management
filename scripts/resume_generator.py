#!/usr/bin/env python3
"""Generate tailored resumes for Notion-tracked jobs using Gemini API."""

import json
import os
import re
import sys

import requests
from asset_retriever import find_code_block, get_block_children
from google import genai
from weasyprint import HTML
from util import ROOT, load_config, load_env, notion_headers

MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.1-pro-preview")

SYSTEM_PROMPT = (
    "You are an expert ATS resume writer. You produce clean, well-structured HTML "
    "resumes tailored to specific job descriptions. You always output pure HTML with "
    "no markdown wrapping, no code fences, and no explanatory text. You are meticulous "
    "about replacing every placeholder token with real content."
)


def _text(prop):
    arr = prop.get("rich_text") or prop.get("title") or []
    return "".join(t.get("plain_text", "") for t in arr).strip()


def sanitize_filename(name):
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = name.strip(" .")
    if len(name) > 200:
        name = name[:200]
    return name


def query_pages_by_status(db_id, status_name, h):
    results = []
    cursor = None
    while True:
        payload = {
            "page_size": 100,
            "filter": {
                "property": "Status",
                "status": {"equals": status_name},
            },
        }
        if cursor:
            payload["start_cursor"] = cursor
        r = requests.post(
            f"https://api.notion.com/v1/databases/{db_id}/query",
            headers=h,
            data=json.dumps(payload),
            timeout=30,
        ).json()
        results.extend(r.get("results", []))
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
    return results


def extract_page_properties(page):
    props = page.get("properties", {})
    return {
        "page_id": page.get("id"),
        "company": _text(props.get("Name", {})),
        "position": _text(props.get("position", {})),
        "url": props.get("URL", {}).get("url", ""),
    }


def reconstruct_jd(page_id, h):
    children = get_block_children(page_id, h)
    paragraphs = []
    for block in children:
        if block.get("type") == "paragraph":
            content = _text(block.get("paragraph", {}))
            if content:
                paragraphs.append(content)
    return "\n\n".join(paragraphs)


def has_placeholders(html):
    return bool(re.search(r"\[[A-Z][a-zA-Z\s]*\]", html))


def generate_resume(master_html, template_html, company, position, jd_text, api_key):
    client = genai.Client(api_key=api_key)
    user_prompt = f"""Generate a tailored resume for the following job opportunity.

## Instructions

1. Use the EXACT HTML structure and CSS styling from the Resume Template below. Do not alter the layout, font styles, colors, section ordering, or any visual formatting.
2. Select and adapt content from the Master Resume that is most relevant to the target Job Description. Prioritize skills, technologies, and experiences that match keywords in the JD. Every bullet and sentence must be high-impact — lead with results, and action verbs.
3. Replace ALL bracketed placeholder tokens in the template with actual values:
   - [Company] → {company}
   - [Position] → {position}
   - Any other [placeholder] → an appropriate real value from the master resume
4. Tailor the Professional Profile / Summary section to align with the specific requirements and language of the job description. Keep it to 3 sentences maximum — punchy, concise, and high-impact. No fluff.
5. Keep all content truthful — only use information present in the Master Resume. Do not fabricate experience, skills, or achievements.
6. Output ONLY pure HTML. No markdown fences, no explanations, no preamble.

## Target Job

- Company: {company}
- Position: {position}

## Job Description

{jd_text}

## Resume Template (FOLLOW THIS FORMAT EXACTLY)

{template_html}

## Master Resume (SOURCE OF ALL CONTENT)

{master_html}"""

    response = client.models.generate_content(
        model=MODEL,
        contents=user_prompt,
        config={
            "system_instruction": SYSTEM_PROMPT,
            "max_output_tokens": 8192,
        },
    )
    return response.text


def update_page_status(page_id, status_name, note_text, h):
    payload = {
        "properties": {
            "Status": {"status": {"name": status_name}},
            "note": {"rich_text": [{"type": "text", "text": {"content": note_text[:2000]}}]},
        }
    }
    requests.patch(
        f"https://api.notion.com/v1/pages/{page_id}",
        headers=h,
        data=json.dumps(payload),
        timeout=30,
    )


def run(env_path=None, output_dir=None):
    if env_path is None:
        env_path = str(ROOT / ".env")
    if output_dir is None:
        output_dir = str(ROOT / "generated_resumes")

    load_env(env_path)

    token = os.environ.get("NOTION_TOKEN")
    db_id = os.environ.get("DB_ID")
    api_key = os.environ.get("GEMINI_API_KEY")
    if not token or not db_id:
        print("ERROR: NOTION_TOKEN and DB_ID must be set in .env", flush=True)
        sys.exit(1)
    if not api_key:
        print("ERROR: GEMINI_API_KEY must be set in .env", flush=True)
        sys.exit(1)

    if "-" not in db_id and len(db_id) == 32:
        db_id = f"{db_id[:8]}-{db_id[8:12]}-{db_id[12:16]}-{db_id[16:20]}-{db_id[20:]}"

    h = notion_headers(token)
    cfg = load_config()
    master_page_id = cfg["notion"]["master_resume_page_id"]
    template_page_id = cfg["notion"]["resume_template_page_id"]

    master_html = find_code_block(master_page_id, h)
    template_html = find_code_block(template_page_id, h)
    if not master_html:
        print("ERROR: No code block found on master resume page", flush=True)
        sys.exit(1)
    if not template_html:
        print("ERROR: No code block found on resume template page", flush=True)
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    pages = query_pages_by_status(db_id, "Not started", h)
    if not pages:
        print("No pages with Status='Not started' found.")
        return {"total": 0, "success": 0, "error": 0, "errors": [], "output_dir": output_dir}

    print(f"Found {len(pages)} page(s) with Status='Not started'", flush=True)

    summary = {"total": len(pages), "success": 0, "error": 0, "errors": [], "output_dir": output_dir}

    for page in pages:
        try:
            job = extract_page_properties(page)
            if not job["company"] or not job["position"]:
                raise ValueError("Missing company or position value")

            job["jd_text"] = reconstruct_jd(job["page_id"], h)

            html = generate_resume(
                master_html, template_html,
                job["company"], job["position"], job["jd_text"], api_key,
            )

            for attempt in range(5):
                if not has_placeholders(html):
                    break
                html = generate_resume(
                    master_html, template_html,
                    job["company"], job["position"], job["jd_text"], api_key,
                )

            if has_placeholders(html):
                raise RuntimeError("Generated resume still contains placeholder tokens after 5 retries")

            safe_company = sanitize_filename(job["company"])
            safe_position = sanitize_filename(job["position"])
            filename = f"{safe_company} - {safe_position} Resume.html"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)

            pdf_path = filepath.rsplit(".", 1)[0] + ".pdf"
            HTML(string=html).write_pdf(pdf_path)

            update_page_status(job["page_id"], "resume", f"Resume saved: {filename}", h)
            summary["success"] += 1
            print(f"[OK] {job['company']} — {job['position']}", flush=True)

        except Exception as exc:
            error_msg = f"{type(exc).__name__}: {exc}"
            summary["error"] += 1
            summary["errors"].append({
                "company": job.get("company", "unknown"),
                "position": job.get("position", "unknown"),
                "error": error_msg,
            })
            try:
                update_page_status(job.get("page_id"), "Error", str(exc)[:1900], h)
            except Exception as update_err:
                print(f"[WARN] Could not update error status: {update_err}", flush=True)
            print(f"[FAIL] {job.get('company', '?')} — {job.get('position', '?')}: {exc}", flush=True)

    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    run()
