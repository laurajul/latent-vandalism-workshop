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
