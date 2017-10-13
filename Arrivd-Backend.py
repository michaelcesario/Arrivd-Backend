from flask import Flask, jsonify
from flask_restful import Api
from Resources.User import User

app = Flask(__name__)
app.secret_key = 'test_key'
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


api.add_resource(User, '/user/<string:username>')

if __name__ == '__main__':
    app.run()
