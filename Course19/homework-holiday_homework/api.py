from http.server import HTTPServer, BaseHTTPRequestHandler
from flower_shop import FlowerShop, Tulip
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
      #extract the key content-length frm headers
      length = self.headers.get('content-length')
      print(length)
      #read the request data
      data = self.rfile.read(int(length))
      decoded_data = json.loads(data.decode())
      if decoded_data['type'] == 'Tulip':
          flowers = [Tulip(decoded_data['color'], decoded_data['number'])]
      FlowerShop().add_to_inventory(flowers)
      print(decoded_data['type'])
      self.prepare_response()



server_address = ('127.0.0.1', 8000)
server = HTTPServer(server_address, FlowerRequestHandler)
server.serve_forever()