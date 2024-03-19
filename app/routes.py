from flask import render_template, redirect, url_for, session, abort
from app.forms import SimpleForm
from models import Role, User

from app import flask_app


@flask_app.route('/')
@flask_app.route('/index')
def index():
    default_user = {"username": "Alex"}
    session_text = session.get('text')
    if session_text is not None or session_text != "":
        return render_template("index.html", text=session_text, auth=session.get('auth'))
    else:
        return render_template('index.html', user=default_user, auth=session.get('auth'))

@flask_app.errorhandler(404)
def page_not_found(e):
    return render_template("404_temp.html"), 404

@flask_app.errorhandler(400)
def error_request(e):
    pass
    # return render_template("templ"), 400

@flask_app.route("/error")
def test_error():
    abort (404)

@flask_app.route('/testForm', methods=['GET','POST'])
def testForm():
    text = None
    form = SimpleForm()
    if form.validate_on_submit():
        print(form.username.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            print("Test")
            session['auth'] = True
        else:
            session['auth'] = False
        return redirect(url_for('index'))
    return render_template('formTemplate.html', form=form, text=text, auth=session.get('auth'))

@flask_app.route('/logout')
def logout():
    if session.get('auth'):
        session['auth'] = False
    return redirect(url_for('index'))
