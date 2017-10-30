from flask import jsonify
import constants
import psycopg2

class UserModel:

    def __init__(self, _id, username, phoneNumber, password):
        self.username = username
        self.phoneNumber = phoneNumber
        self.password = password
        self.id = _id

    def json(self):
        userJSON = {
            "username": self.username,
            "phoneNumber": self.phoneNumber
        }
        return userJSON

    @classmethod
    def findByUsername(cls, username):
        dbConnection = psycopg2.connect(database=constants.dbName, user=constants.dbUser, password=constants.dbPassword, host=constants.dbHost)
        cursor = dbConnection.cursor()

        query = "select * from users where username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        dbConnection.close()

        return UserModel(result[0], result[1], result[2], result[3]) if result else None


    @classmethod
    def findByID(cls, ID):
        dbConnection = psycopg2.connect(database=constants.dbName, user=constants.dbUser, password=constants.dbPassword, host=constants.dbHost)
        cursor = dbConnection.cursor()

        findUserQuery = "select * from users where id = %s;"
        cursor.execute(findUserQuery, (ID,))
        result = cursor.fetchone()
        dbConnection.close()

        return UserModel(result[0], result[1], result[2], result[3]) if result else None
