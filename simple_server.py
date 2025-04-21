import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

print(f"Starting server on port {PORT}...")
print(f"Try accessing: http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server running...")
    httpd.serve_forever()