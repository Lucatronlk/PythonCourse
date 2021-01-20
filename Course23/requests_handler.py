from http.server import BaseHTTPRequestHandler


class OurHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print('get request')
        if self.path == '/hello':
            print('hello request')
            self.__send_200_response()
            #write the response
            self.wfile.write(b'Hello World!')

    def __send_200_response(self):
        # put the status code 200 ( means ok )
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        # end the header space
        self.end_headers()

    def do_POST(self):
        print('post request')
        if self.path == '/file':
            print('file endpoint')
            file_name = self.headers.get('file_name')
            print("file name: " + file_name)
            file = open(file_name, 'w')
            file.close()
            self.__send_200_response()
