import psycopg2
from flask_restful import Resource, reqparse


class User(Resource):

    def get(self, username):
        dbConnection = psycopg2.connect(database="arrivd", user="postgres", password="<password here>", host="localhost")
        cursor = dbConnection.cursor()

        query = "select * from users where username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        dbConnection.close()

        print(result)
        if result:
            return {
                "username": result[0],
                "phoneNumber": result[1]
            }
        else:
            return {"message": "user not found"}