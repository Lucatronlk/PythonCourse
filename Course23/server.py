from http.server import HTTPServer,BaseHTTPRequestHandler
from requests_handler import  OurHandler

#if we exectute the file only what`s here it will be executed
if __name__ == "__main__":
    server_address = ('localhost', 8000)
    http_server = HTTPServer(server_address, OurHandler)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass

    http_server.server_close()


