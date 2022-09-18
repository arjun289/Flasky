from os import abort
from flask import Flask, render_template
from flask import request
from flask import make_response


app = Flask(__name__)


@app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response
def index():
    return render_template('index.html')

app.add_url_rule('/', 'index', index)

@app.route('/user/<name>')
# def user(name):
#     return '<h1>hello, {}!</h1>'.format(name)
def user(name):
    return render_template('user.html', name=name)

@app.route('/user/<int:id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)
