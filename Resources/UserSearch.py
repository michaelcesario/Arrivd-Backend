import psycopg2
import constants
from flask_restful import Resource, reqparse
from Models.UserModel import UserModel
from flask_jwt import jwt_required

class UserSearch(Resource):

    #@jwt_required()
    def post(self, partialMatch):
        dbConnection = psycopg2.connect(database=constants.dbName, user=constants.dbUser, password=constants.dbPassword,
                                        host=constants.dbHost)
        cursor = dbConnection.cursor()

        partialMatch = '%' + str(partialMatch).lower() + '%'
        query = "select id, username from users where LOWER(username) like %s"
        cursor.execute(query, (partialMatch,))
        result = cursor.fetchall()
        dbConnection.close()

        users = {}
        for user in result:
            users[user[0]] = {"id": user[0], "username": user[1]}

        print(users)
        return users
