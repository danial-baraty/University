# BaseHTTPRequestHandler: A base class for handling HTTP requests in a server.
# HTTPServer: A simple HTTP server class that listens for requests and uses a handler to process them.

from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)

        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(b"THIS IS AN UNENCRYPTED TEXT!")


# This ensures that the code following the if __name__ == "__main__": block is only executed when the file is run directly, not when it is imported as a module in another file.
if __name__ == "__main__":
    server_address = ("127.0.0.1", 8000) 
    # When a GET request is sent to the server, HTTPServer creates an object from the handler class (in this case, SimpleHandler) and calls its do_GET method to process the request.
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server running at http://127.0.0.1:8000/")
    httpd.serve_forever()