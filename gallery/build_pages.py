#!/usr/bin/env python3
"""Assemble the GitHub Pages site into an output folder.

    docs/*                      -> <out>/
    gallery/{index.html,...}    -> <out>/gallery/
    gallery/images/*            -> <out>/gallery/images/
    (generated)                 -> <out>/gallery/images.json   newest first

Pages is static, so the gallery reads images.json instead of asking serve.py to scan a folder.
Newest first means most recently committed, so drop new images into gallery/images/ and push.

Usage:
    python3 gallery/build_pages.py _site
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GALLERY_SRC = ROOT / "gallery"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"}
GALLERY_FILES = ["index.html", "style.css", "app.js"]


def commit_time(path: Path) -> int:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", str(path)],
        cwd=ROOT, capture_output=True, text=True,
    )
    text = result.stdout.strip()
    return int(text) if text else int(path.stat().st_mtime)


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    out = Path(sys.argv[1]).resolve()
    if out.exists():
        shutil.rmtree(out)

    shutil.copytree(ROOT / "docs", out)

    gallery_out = out / "gallery"
    (gallery_out / "images").mkdir(parents=True)
    for name in GALLERY_FILES:
        shutil.copy(GALLERY_SRC / name, gallery_out / name)

    images = sorted(
        (f for f in (GALLERY_SRC / "images").glob("*")
         if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS),
        key=commit_time,
        reverse=True,
    )
    for f in images:
        shutil.copy(f, gallery_out / "images" / f.name)
    (gallery_out / "images.json").write_text(
        json.dumps([{"name": f.name} for f in images]), encoding="utf-8"
    )
    print(f"Built {out} with {len(images)} gallery image(s)")


if __name__ == "__main__":
    main()
