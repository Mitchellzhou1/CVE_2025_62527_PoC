from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from urllib.parse import urlparse, parse_qs

class LoggingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        logging.info("=== Incoming GET ===")
        logging.info(f"Path: {parsed.path}")
        logging.info(f"Query: {parse_qs(parsed.query)}")
        logging.info(f"Headers:\n{self.headers}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK\n")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        logging.info("=== Incoming POST ===")
        logging.info(f"Body: {post_data.decode(errors='ignore')}")
        logging.info(f"Headers:\n{self.headers}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK\n")

server = HTTPServer(('0.0.0.0', 80), LoggingHandler)
print("Listening...")
server.serve_forever()

