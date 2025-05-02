# HTTP and HTTPS Servers

This project includes two server implementations:

- An HTTP server using Python's built-in `http.server` module.
- An HTTPS server using Python's `socket` and `ssl` modules.

These servers simply output a basic message to the client upon receiving a request.

## HTTPS Setup

Before generating certificate files, make sure OpenSSL is installed on your system. You can download OpenSSL for Windows from the following trusted source:

- [Win32/Win64 OpenSSL Installer by Shining Light Productions](https://slproweb.com/products/Win32OpenSSL.html)[](https://slproweb.com/products/Win32OpenSSL.html)

To generate the SSL certificate and private key, run the following command in Git Bash or your terminal:

```bash
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout key.pem -out cert.pem
```

## Testing the Servers

After running the servers, you can send requests to them using `curl` from Git Bash or your terminal.

- For the HTTP server (running on port 8000):
  ```bash
  curl http://localhost:8000
  ```

- For the HTTPS server (running on port 8443):
  ```bash
  curl -k https://localhost:8443
  ```

You can use these commands to test the servers after starting them. The servers will respond with a simple message displayed in the client output.