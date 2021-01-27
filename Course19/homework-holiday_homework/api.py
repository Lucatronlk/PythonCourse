from http.server import HTTPServer, BaseHTTPRequestHandler
from flower_shop import FlowerShop
import json

class FlowerRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
      print('Am ajuns in GET')
      self.prepare_response()

  def prepare_response(self):
      self.send_response(200)
      self.send_header('Content-type', 'application/json')
      self.end_headers()
      self.list_inventory()

  def list_inventory(self):
      inventory = FlowerShop().get_invetory()  # create the instance inline
      # call __dict__ on the flowe objects in json.dumps
      inventory_json = json.dumps(inventory, default=lambda x: x.type)
      to_bytes = inventory_json.encode
      print(to_bytes)
      self.wfile.write(to_bytes())

  def do_POST(self):
      print("Am ajuns in POST")
      length = self.headers.get('content-legth')
      print(length)
      print(self.rfile.read(int(length)))
      self.prepare_response()



server_address = ('127.0.0.1', 8000)
server = HTTPServer(server_address, FlowerRequestHandler)
server.serve_forever()