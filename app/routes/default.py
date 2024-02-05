from .. import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/items")
def items():
    context = {
        "items": [1, 2, 3, 4, 5]
    }
    return render_template("list.html", **context)