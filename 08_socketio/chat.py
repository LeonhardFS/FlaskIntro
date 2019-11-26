from flask import Flask
from flask import render_template, redirect, request, url_for, flash
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
Bootstrap(app)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print('hello world')
    socketio.run(app, debug=True)
