from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = int(os.environ.get("PORT", 8000))
FOLDER = "."  # Usa "." para la raíz del proyecto, o "src/" si tus HTML están en una subcarpeta

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FOLDER, **kwargs)

with HTTPServer(("", PORT), Handler) as httpd:
    print(f"Servidor iniciado en http://localhost:{PORT}")
    httpd.serve_forever()