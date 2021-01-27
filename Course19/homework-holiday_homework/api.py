from http.server import HTTPServer, BaseHTTPRequestHandler

class FlowerRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
      pass

  def do_POST(self):
      pass


server_address = ('locahost', 8000)
server = HTTPServer(server_address, FlowerRequestHandler)
server.serve_forever()