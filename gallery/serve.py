#!/usr/bin/env python3
"""Local image gallery server.

Serves a directory of images (e.g. a Google Drive desktop-synced folder) as a
grid in the browser. The folder is scanned fresh on every request, so newly
synced images just show up on refresh. Stdlib only — no dependencies, no
network calls beyond localhost.

Usage:
    python3 serve.py /path/to/synced/drive/folder [--port 8000]
"""
import argparse
import json
import mimetypes
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

GALLERY_DIR = Path(__file__).parent
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"}
STATIC_FILES = {
    "/": ("index.html", "text/html"),
    "/index.html": ("index.html", "text/html"),
    "/style.css": ("style.css", "text/css"),
    "/app.js": ("app.js", "application/javascript"),
}


def make_handler(image_dir: Path):
    class GalleryHandler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            pass  # keep stdout quiet

        def do_GET(self):
            path = unquote(urlparse(self.path).path)

            if path in STATIC_FILES:
                name, content_type = STATIC_FILES[path]
                return self._serve_file(GALLERY_DIR / name, content_type)
            if path == "/api/images":
                return self._serve_image_list()
            if path.startswith("/images/"):
                return self._serve_image(path[len("/images/"):])

            self.send_error(404)

        def _serve_file(self, file_path: Path, content_type: str):
            if not file_path.is_file():
                self.send_error(404)
                return
            data = file_path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", f"{content_type}; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _serve_image_list(self):
            files = sorted(
                (f for f in image_dir.iterdir()
                 if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS),
                key=lambda f: f.stat().st_mtime,
                reverse=True,
            )
            body = json.dumps([{"name": f.name} for f in files]).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _serve_image(self, name: str):
            image_root = image_dir.resolve()
            file_path = (image_root / name).resolve()
            if not file_path.is_relative_to(image_root):
                self.send_error(403)
                return
            if not file_path.is_file() or file_path.suffix.lower() not in IMAGE_EXTENSIONS:
                self.send_error(404)
                return
            content_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
            data = file_path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    return GalleryHandler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "image_dir", type=Path, nargs="?",
        default=Path("/home/lauhp/GoogleDrive/latent_vandalism_models/Gallery"),
        help="Folder of images to display (default: %(default)s)",
    )
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    image_dir = args.image_dir.expanduser().resolve()
    if not image_dir.is_dir():
        raise SystemExit(f"Not a directory: {image_dir}")

    server = ThreadingHTTPServer(("localhost", args.port), make_handler(image_dir))
    print(f"Serving images from {image_dir}")
    print(f"Open http://localhost:{args.port} in your browser (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
