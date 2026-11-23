#!/usr/bin/env python3
"""Lokaler Server für _book/, der dem Browser das Zwischenspeichern verbietet.

Aufruf (aus dem Repo-Root):  python3 scripts/serve.py [PORT]   (Standard: 8001)
Nach jedem `quarto render` zeigt ein normales Neuladen sofort die neue Fassung.
"""
import functools
import http.server
import pathlib
import sys


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # no-store = Browser darf keine Kopie behalten, fragt jedes Mal neu
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8001
root = pathlib.Path(__file__).resolve().parent.parent / "_book"
handler = functools.partial(NoCacheHandler, directory=str(root))
print(f"Serving {root} on http://127.0.0.1:{port}/  (Ctrl+C beendet)")
http.server.ThreadingHTTPServer(("127.0.0.1", port), handler).serve_forever()
