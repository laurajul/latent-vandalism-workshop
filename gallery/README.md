# Gallery

A local grid viewer for a folder of images — e.g. the folder your Google Drive desktop app syncs
to disk. No backend to deploy, no API keys, no network calls beyond localhost: `serve.py` scans
the folder fresh on every request, so newly synced images just show up on refresh.

## Usage

```
python3 gallery/serve.py "/path/to/your/synced/drive/folder"
```

Then open `http://localhost:8000` in your browser. Use `--port` to pick a different port.

Requires only the Python 3 standard library — no `pip install` needed.

## On GitHub Pages

The same page is published at `.../gallery/` alongside the instructions page. Pages is static,
so instead of scanning a folder it reads a manifest that the workflow generates
(`gallery/build_pages.py`) from the images committed in `gallery/images/`, newest commit first.

To add images: copy them into `gallery/images/`, commit, and push. The workflow republishes on
every push that touches `gallery/` or `docs/`.
