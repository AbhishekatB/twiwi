from http.server import BaseHTTPRequestHandler
import json
from function import get_user_tweets, fetch_user_data

class handler(BaseHTTPRequestHandler):
    routes = {
        '/api/get_user_tweets': get_user_tweets,
        '/api/fetch_user_data': fetch_user_data,
        # Add more routes and functions here
    }
    
    def _send_response(self, status_code, response_data):
        """Helper to send the response"""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())
    
    def do_GET(self):
        """Handle GET requests"""
        # Determine route based on the request path
        if self.path in self.routes:
            function = self.routes[self.path]
            # Call the corresponding function (you can modify this to pass parameters from query string)
            result = function()
            self._send_response(200, result)
        else:
            self._send_response(404, {"error": "Not Found"})
    
    def do_POST(self):
        """Handle POST requests"""
        # Determine route based on the request path
        if self.path in self.routes:
            function = self.routes[self.path]
            # Read and parse the incoming JSON body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())
            # Call the corresponding function and pass the data (for example, username in the POST body)
            result = function(**data)
            self._send_response(200, result)
        else:
            self._send_response(404, {"error": "Not Found"})
