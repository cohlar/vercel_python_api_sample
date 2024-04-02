from http.server import BaseHTTPRequestHandler
import pandas as pd

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        df = pd.DataFrame()

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return