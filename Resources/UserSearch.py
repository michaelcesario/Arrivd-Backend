import psycopg2
import constants
from flask_restful import Resource, reqparse
from db import DatabaseConnection

class UserSearch(Resource):

    #@jwt_required()
    def post(self, partialMatch):
        cursor = DatabaseConnection.getDBCursor()

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
