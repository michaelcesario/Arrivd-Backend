import psycopg2
from flask_restful import Resource, reqparse
from Models.UserModel import UserModel

class User(Resource):

    def get(self, username):
        dbConnection = psycopg2.connect(database="arrivd", user="postgres", password="<password here>", host="localhost")
        cursor = dbConnection.cursor()

        query = "select * from users where username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        dbConnection.close()

        user = UserModel(result[0], result[1])
        if result:
            return user.json()
        else:
            return {"message": "user not found"}
