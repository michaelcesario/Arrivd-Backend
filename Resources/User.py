from flask_restful import Resource, reqparse
from Models.UserModel import UserModel
from flask_jwt import jwt_required
from db import DatabaseConnection

class User(Resource):

    @jwt_required()
    def get(self, username):
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        queryUsername = "select * from users where username = %s"
        cursor.execute(queryUsername, (username,))
        result1 = cursor.fetchone()

        queryNumber = "select * from users where phonenumber = %s"
        cursor.execute(queryNumber, (username,))
        result2 = cursor.fetchone()

        dbConnection.close()

        if result1:
            user = UserModel(result1[0], result1[1], result1[2], result1[3])
            return user.json()
        elif result2:
            user = UserModel(result2[0], result2[1], result2[2], result2[3])
            return user.json()
        else:
            return {"message": "user not found"}
