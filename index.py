# index.py

from http.server import BaseHTTPRequestHandler
from api.function import handle_get, handle_post
import json

class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Call the function from functions.py to handle GET
        response_data = handle_get()

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())
        return

    def do_POST(self):
        # Get the content length and read POST data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Parse the incoming JSON data
        data = json.loads(post_data.decode())

        # Call the function from functions.py to handle POST
        response_data = handle_post(data)

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())
        return
