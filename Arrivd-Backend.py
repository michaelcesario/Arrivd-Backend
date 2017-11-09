from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from Resources.User import User
from Resources.Notification import Notification
from Resources.RegisterUser import RegisterUser
from Resources.NotificationTrigger import NotificationTrigger
from Resources.UserSearch import UserSearch
from Resources.Pending import Pending
from Resources.Delivered import Delivered
from Resources.Test import Test
from Resources.APNS import APNS
from security import authenticate, identity

from db import DatabaseConnection

c = DatabaseConnection.getDBCursor()

app = Flask(__name__)
app.secret_key = 'test_key'
api = Api(app)

jwt = JWT(app, authenticate, identity)

@app.route('/')
def hello_world():

    return 'Hello World!'


api.add_resource(User, '/user/<string:username>')
api.add_resource(Pending, '/user/<int:id>/pending')
api.add_resource(Delivered, '/user/<int:id>/delivered')
api.add_resource(RegisterUser, '/register')
api.add_resource(Notification, '/notification')
api.add_resource(NotificationTrigger, '/trigger-notification/<int:id>')
api.add_resource(UserSearch, '/search-user/<string:partialMatch>')
api.add_resource(Test, '/test')
api.add_resource(APNS, '/apns/<int:id>')

if __name__ == '__main__':
    app.run()
