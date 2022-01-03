from flask import Flask, render_template, request, redirect, Response
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def chat():
    cookies = request.cookies
    if not 'name' in cookies:
        return render_template('select_name.html')
    else:
        return render_template('chat.html', name=cookies['name'])

@app.route('/set_name/<string:name>')
def set_name(name):
    resp = redirect('/')
    resp.set_cookie('name', name)
    return resp

@socketio.on('msg')
def msg(data):
    if not data['msg'] == '':
        socketio.emit('msg', data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8074, debug=True)
