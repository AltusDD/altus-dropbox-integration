
import re
import time

def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "unnamed"

def safe_filename(name: str) -> str:
    name = name.strip()
    name = re.sub(r"[\\/:*?\"<>|]", "_", name)
    name = re.sub(r"\s+", "_", name)
    return name or "file"

def stamped_filename(original: str) -> str:
    base = safe_filename(original)
    ts = time.strftime("%Y%m%d-%H%M%S")
    return f"{ts}__{base}"
