"""it is an entry point."""
from flask import Flask, render_template


app = Flask(__name__)
# reading a config from the config.py:Config
app.config.from_object('config.Config')


@app.route("/")
def hello_world() -> str:
    """
    Entry point of out brand new powerful backend.

    (this is stored in __doc__ and can be accessed through help function)
    """
    return render_template('hello.html', name=__name__)
