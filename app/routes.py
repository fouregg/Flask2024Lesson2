from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Alex"}
    return render_template("index.html", user=user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(400)
def error_request(e):
    pass
    # return render_template("templ"), 400
