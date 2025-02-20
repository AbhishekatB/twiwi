from http.server import BaseHTTPRequestHandler
from os.path import join
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response code to 200 (OK)
        self.send_response(200)
        
        # Set headers (you can change the content type depending on your data)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Define the response data (you could also use files or other resources)
        response_data = {"message": "Hello from the Python API!"}
        
        # Send the JSON data as the response
        self.wfile.write(json.dumps(response_data).encode())
        return

    def do_POST(self):
        # Similar setup for POST requests
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Handle the incoming JSON data
        data = json.loads(post_data.decode())

        # You can process the data here
        response_data = {"received": data}

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())
        return
