import psycopg2
from flask_restful import Resource, reqparse
from Models.UserModel import UserModel

class RegisterUser(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be blank')
    parser.add_argument('phoneNumber', type=str, required=True)

    def post(self):
        userData = RegisterUser.parser.parse_args()
        print(userData)

        if UserModel.findByUsername(userData['username']):
            return {"message": "Username already exists"}

        dbConnection = psycopg2.connect(database="arrivd", user="postgres", password="", host="localhost")
        cursor = dbConnection.cursor()

        query = "INSERT INTO users(username, phonenumber, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (userData['username'], userData['phoneNumber'], userData['password']))

        dbConnection.commit()
        dbConnection.close()

        return {"message": "User created successfully"}