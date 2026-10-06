#!/usr/bin/env python3
"""Serve Fluent in Kid to every device on your local network.

Usage:  python3 serve.py [port]     (default port 8080)
Then open the printed http://<your-ip>:<port> address on any phone,
tablet or computer on the same Wi-Fi.
"""
import http.server
import socket
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGE = HERE / "fluent-in-kid.html"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

SKELETON = (
    "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">"
    "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>"
    "</head><body>{content}</body></html>"
)


def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))  # no packet is sent; just picks the LAN interface
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] not in ("/", "/index.html"):
            self.send_error(404)
            return
        # Re-read on every request so edits to the page show up on refresh.
        body = SKELETON.replace("{content}", PAGE.read_text(encoding="utf-8")).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"{self.client_address[0]}  {fmt % args}")


if __name__ == "__main__":
    server = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print("Fluent in Kid is running.")
    print(f"  On this computer:  http://localhost:{PORT}")
    print(f"  On your network:   http://{lan_ip()}:{PORT}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
