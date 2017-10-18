from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from Resources.User import User
from Resources.Notification import Notification
from Resources.RegisterUser import RegisterUser
from Resources.SendNotification import NotificationTrigger
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'test_key'
api = Api(app)

jwt = JWT(app, authenticate, identity)

@app.route('/')
def hello_world():
    return 'Hello World!'


api.add_resource(User, '/user/<string:username>')
api.add_resource(RegisterUser, '/register')
api.add_resource(Notification, '/notification')
api.add_resource(NotificationTrigger, '/trigger-notification/<int:id>')

if __name__ == '__main__':
    app.run()
