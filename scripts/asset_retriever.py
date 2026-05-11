#!/usr/bin/env python3
"""Retrieve the HTML code block from a Notion page."""

import argparse
import os

import requests

from util import load_config, load_env, notion_headers, ROOT


def get_block_children(block_id, h):
    children = []
    cursor = None
    while True:
        url = f"https://api.notion.com/v1/blocks/{block_id}/children?page_size=100"
        if cursor:
            url += f"&start_cursor={cursor}"
        r = requests.get(url, headers=h, timeout=30).json()
        children.extend(r.get("results", []))
        if not r.get("has_more"):
            break
        cursor = r.get("next_cursor")
    return children


def find_code_block(page_id, h):
    blocks = get_block_children(page_id, h)
    for block in blocks:
        if block.get("type") == "code":
            rich_text = block.get("code", {}).get("rich_text", [])
            return "".join(t.get("plain_text", "") for t in rich_text)
    return None



if __name__ == "__main__":
    cfg = load_config()

    ap = argparse.ArgumentParser(description="Retrieve HTML code block from a Notion page.")
    ap.add_argument("--env", default=str(ROOT / ".env"), help="Path to .env file")
    ap.add_argument("--page-id", default=cfg["notion"]["master_resume_page_id"],
                    help="Notion page ID (default: Master Resume page)")
    args = ap.parse_args()

    load_env(args.env)
    token = os.environ["NOTION_TOKEN"]
    h = notion_headers(token)

    page_id = args.page_id
    if "-" not in page_id and len(page_id) == 32:
        page_id = f"{page_id[:8]}-{page_id[8:12]}-{page_id[12:16]}-{page_id[16:20]}-{page_id[20:]}"

    html = find_code_block(page_id, h)
    if html is None:
        print("No code block found on the page.")
    else:
        print(html)
