import psycopg2
import constants
from flask_restful import Resource, reqparse
from Models.UserModel import UserModel
from flask_jwt import jwt_required

class User(Resource):

    @jwt_required()
    def get(self, username):
        dbConnection = psycopg2.connect(database=constants.dbName, user=constants.dbUser, password=constants.dbPassword, host=constants.dbHost)
        cursor = dbConnection.cursor()

        query = "select * from users where username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        dbConnection.close()

        print(result)
        user = UserModel(result[0], result[1], result[2], result[3])
        if result:
            return user.json()
        else:
            return {"message": "user not found"}
