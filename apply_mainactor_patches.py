#!/usr/bin/env python3
import json
from pathlib import Path
patches = json.loads(Path(__file__).with_name("patches.json").read_text())
for item in patches:
    path = Path(item["path"])
    old, new = item["old"], item["new"]
    text = path.read_text()
    if old not in text:
        raise SystemExit(f"MISSING pattern in {path}")
    path.write_text(text.replace(old, new, 1))
    print(f"patched {path}")
print(f"all {len(patches)} patches applied")
