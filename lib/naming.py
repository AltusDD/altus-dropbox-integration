import re, unicodedata, time, random, string

def slugify(value: str) -> str:
    if value is None:
        return "unknown"
    value = str(value)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value or "unknown"

def unique_filename(original: str) -> str:
    # append short stamp to avoid collisions
    base, dot, ext = original.rpartition(".")
    stamp = f"{int(time.time())}-{random.randrange(1000,9999)}"
    if dot:
        return f"{base}-{stamp}.{ext}"
    else:
        return f"{original}-{stamp}"
