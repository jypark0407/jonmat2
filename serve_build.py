import os
from http.server import HTTPServer, SimpleHTTPRequestHandler


BASE_DIR = os.path.dirname(__file__)


class CustomHandler(SimpleHTTPRequestHandler):
    def guess_type(self, path):
        mimetype = SimpleHTTPRequestHandler.guess_type(self, path)

        if mimetype == 'application/octet-stream':
            relpath = os.path.relpath(path, BASE_DIR)
            if relpath.startswith('who') or relpath.startswith('where'):
                return 'text/html'

        return mimetype

os.chdir('./build')
server = HTTPServer(('0.0.0.0', 8009), CustomHandler)
server.serve_forever()
