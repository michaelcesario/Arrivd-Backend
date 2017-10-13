from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from Resources.User import User
from Resources.RegisterUser import RegisterUser
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'test_key'
api = Api(app)

jwt = JWT(app, authenticate, identity)

@app.route('/')
def hello_world():
    return 'Hello World!'


api.add_resource(User, '/user/<string:username>')
api.add_resource(RegisterUser, '/user/register')

if __name__ == '__main__':
    app.run()
