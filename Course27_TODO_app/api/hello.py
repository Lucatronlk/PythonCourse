import flask

server = flask.Flask(__name__)

# define an API endpoint
@server.route('/hello')
def hello():
    return 'Hello World'

