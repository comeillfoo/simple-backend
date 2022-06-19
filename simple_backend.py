"""it is an entry point."""
from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
# reading a config from the config.py:Config
app.config.from_object('config.Config')

socketio = SocketIO(app, cors_allowed_origin='*')


@socketio.on('message')
def evaluate(data):
    """It's the function that should add two numbers."""
    print(data)
    first_term = int(data['first_term'])
    second_term = int(data['second_term'])
    send(first_term + second_term, broadcast=False)


@app.route("/")
def hello_world() -> str:
    """
    Entry point of out brand new powerful backend.

    (this is stored in __doc__ and can be accessed through help function)
    """
    return render_template('hello.html', name=__name__)
