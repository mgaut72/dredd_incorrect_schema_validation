from flask import Flask
from flask.json import jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def session_handler():
    data = {'expires': 'this should fail since its a string',
            'token'  : 'this should pass since its a string'}
    return jsonify(data=data)

if __name__ == '__main__':
            app.run()
