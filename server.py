from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler, HTTPServer
import json

# Define the server address and port
host = 'localhost'
port = 8000

# Custom handler needed as SimpleHTTPRequestHandler does not handle POST
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get size of incoming data payload
        content_length = int(self.headers['Content-Length'])

        # Read and decode JSON data
        post_data = self.rfile.read(content_length).decode('utf-8') #self.rfile contains the recieved JSON data so content_length provides how many bytes to read
        data = json.loads(post_data)
        print(f"Received POST data: {data}")

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"status": "success", "received": data}).encode('utf-8'))


# Set up the server
server = HTTPServer((host, port), MyRequestHandler)
print(f"Server running at http://{host}:{port}")

# Run the server
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down the server...")
    server.server_close()
