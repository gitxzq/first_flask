#coding=utf-8
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager=Manager(app)


@app.route('/')
def index():
    return 'Hello dalao!'

@app.route('/user/<name>')
def user(name):
    return 'Hello %s !' % name

if __name__ == '__main__':
    # app.run(debug=T
    manager.run()