from http.server import HTTPServer
from api import ToDO


#if we exectute the file only what`s here it will be executed
if __name__ == "__main__":
    server_address = ('localhost', 8100)
    http_server = HTTPServer(server_address, ToDO)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass

    http_server.server_close()
