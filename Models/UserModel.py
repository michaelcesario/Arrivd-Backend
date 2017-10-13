from flask import jsonify

class UserModel:

    def __init__(self, username, phoneNumber):
        self.username = username
        self.phoneNumber = phoneNumber

    def json(self):
        userJSON = {
            "username": self.username,
            "phoneNumber": self.phoneNumber
        }
        return userJSON