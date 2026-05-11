import os
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent


def load_config(path=None):
    if path is None:
        path = ROOT / "config.yml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_env(env_path):
    for line in Path(env_path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ[k] = v.strip().strip('"').strip("'")


def notion_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }
