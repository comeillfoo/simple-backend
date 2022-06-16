"""it is an entry point."""
from flask import Flask


app = Flask(__name__)
# reading a config from the config.py:Config
app.config.from_object('config.Config')


@app.route("/")
def hello_world() -> str:
    """
    Entry point of out brand new powerful backend.

    (this is stored in __doc__ and can be accessed through help function)
    """
    return f"<p>[ {__name__} ]: Hello, World!</p>"
