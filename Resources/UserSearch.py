from flask_restful import Resource, reqparse
from db import DatabaseConnection

class UserSearch(Resource):

    #@jwt_required()
    def post(self, partialMatch):
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        partialMatch = '%' + str(partialMatch).lower() + '%'
        query = "select id, username, apnstoken from users where LOWER(username) like %s"
        cursor.execute(query, (partialMatch,))
        result = cursor.fetchall()
        dbConnection.close()

        users = {}
        for user in result:
            token = True if user[2] else False
            users[user[0]] = {"id": user[0], "username": user[1], "hasAPNSToken": token}

        print(users)
        return users
