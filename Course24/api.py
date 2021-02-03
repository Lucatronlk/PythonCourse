from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import os


class ToDO(BaseHTTPRequestHandler):

    def do_POST(self):
        print("Am ajuns in post")
        self.put_to_do_file()
        self.create_task()


    def put_to_do_file(self):
        if self.path == '/task':
            file_name = self.headers.get('file_name')
            print("file name: " + file_name)
            file = open(file_name, 'w')
            content = self.headers.get('content')
            file.write(content)
            file.close()
            self.send_200_response()



    def create_task(self):

        if self.path == '/task':
            print('start task creation')
            task_number = self.headers('task_number')
            print("task number: " + task_number)



    def do_GET(self):
        print("Am ajuns in GET")
        self.get_response()


    def get_response(self):
        self.send_response(200)


    def do_DELETE(self):
        pass

    def do_PUT(self):
        pass

    def send_200_response(self):
        # put the status code 200 ( means ok )
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        # end the header space
        self.end_headers()



