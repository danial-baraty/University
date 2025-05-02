
# The program is written with two functions to improve structure and maintainability.
# `create_ssl_server()` sets up the server, while `handle_client_connection()` manages client interactions.
# This separation allows for easier updates and debugging, as changes to one part don't affect the other.

import ssl
import socket
from pathlib import Path

def create_ssl_server():
    # SSL Layer
    # SSLContext holds configuration for SSL/TLS connections (certificates, keys, protocols, etc.)
    # It's used to wrap a socket and make it secure.

    # Create an SSL context with the purpose of client authentication (though it's not enforced here)
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    base_dir = Path(__file__).resolve().parent # Returns the directory where the current Python script is located

    cert_path = base_dir / "cert.pem"
    key_path = base_dir / "key.pem"

    # Load the server's certificate and private key into the SSL context
    # key.pem is the server's private key, cert.pem contains the public key (certificate)
    context.load_cert_chain(
    certfile=cert_path, 
    keyfile=key_path
        )
    #TCP Layer
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with SSL to create an SSL server socket
    ssl_server_socket = context.wrap_socket(server_socket, server_side=True)
    ssl_server_socket.bind(('127.0.0.1', 8443))
    ssl_server_socket.listen(5) # When the server is busy and can't immediately accept all requests, it can hold up to 5 clients in the backlog queue
    print("Server listening on port 8443...")
    return ssl_server_socket


def handle_client_connection(ssl_server_socket):
    client_socket, addr = ssl_server_socket.accept()
    print(f"Connection from {addr}")
    data = client_socket.recv(1024)
    # print(f"Received data: {data.decode('utf-8')}")
 
    # Each HTTP header line ends with \r\n; headers end with an empty line: \r\n\r\n
    body = "***HELLO from SSL Server***"
    response = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/plain\r\n"
    f"Content-Length: {len(body)}\r\n"
    "Connection: close\r\n"
    "\r\n"
    f"{body}"
                )
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    # SSL is responsible for securing the connection before passing data to the handler.
    server_socket = create_ssl_server()
    while True:
        handle_client_connection(server_socket)
