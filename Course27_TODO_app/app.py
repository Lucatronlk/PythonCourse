import flask
# '..' == the above folder
from task import Task
from repository import TaskRepository

server = flask.Flask(__name__)

#define an API endpoint
@server.route('/hello')
def hello():
    return 'Hello World'

#define the menu root page
@server.route('/')
def menu():
    template = flask.render_template('menu.html')
    return template

#define what to show when accesing the server/
@server.route('/list')
def main():
    repo = TaskRepository()
    tasks = repo.get()
    print('will show an HTML page')
    paragraph = 'Content of our paragraph'
    html_template = flask.render_template('hello.html', p=paragraph, tasks=tasks)
    print(html_template)
    return html_template

@server.route('/new', methods=('GET', 'POST'))
def new():
    if flask.request.method == 'GET':
        return flask.render_template('new.html')

    if flask.request.method == 'POST':
        new_task = Task(flask.request.form['task-name'],
                        flask.request.form['task-type'])



        repo = TaskRepository()
        repo.add(new_task)
        return flask.redirect(flask.url_for('main'))

