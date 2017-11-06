from flask_restful import Resource, reqparse
from Models.UserModel import UserModel
from passlib.hash import sha256_crypt
from db import DatabaseConnection

class RegisterUser(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('phoneNumber', type=str, required=True)

    def post(self):
        userData = RegisterUser.parser.parse_args()

        if UserModel.findByUsername(userData['username']):
            return {"message": "Username already exists"}, 422

        if UserModel.findByPhoneNumber(userData['phoneNumber']):
            return {"message": "Username already exists"}, 422

        password = sha256_crypt.encrypt(str(userData['password']))

        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        query = "INSERT INTO users(username, phonenumber, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (userData['username'], userData['phoneNumber'], password))

        dbConnection.commit()
        dbConnection.close()

        return {"message": "User created successfully"}