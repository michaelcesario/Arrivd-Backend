import psycopg2
from db import DatabaseConnection

class UserModel:

    def __init__(self, _id, username, phoneNumber, password):
        self.username = username
        self.phoneNumber = phoneNumber
        self.password = password
        self.id = _id

    def json(self):
        userJSON = {
            "username": self.username,
            "phoneNumber": self.phoneNumber,
            "id": self.id
        }
        return userJSON

    @classmethod
    def findByUsername(cls, username):
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        query = "select * from users where username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        dbConnection.close()

        return UserModel(result[0], result[1], result[2], result[3]) if result else None

    @classmethod
    def findByPhoneNumber(cls, phoneNumber):
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        query = "select * from users where phonenumber = %s"
        cursor.execute(query, (phoneNumber,))
        result = cursor.fetchone()
        dbConnection.close()

        return UserModel(result[0], result[1], result[2], result[3]) if result else None

    @classmethod
    def findByID(cls, ID):
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        findUserQuery = "select * from users where id = %s;"
        cursor.execute(findUserQuery, (ID,))
        result = cursor.fetchone()
        dbConnection.close()

        return UserModel(result[0], result[1], result[2], result[3]) if result else None

    @classmethod
    def findPending(cls, id):
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        query = "select receiver, message, date, n.id as notificationID, destination from notifications n join pending p on n.id = p.id and sender = %s"
        cursor.execute(query, (str(id),))

        result = cursor.fetchall()

        pending = []
        for pendingNotification in result:
            receiver = pendingNotification[0]
            message = pendingNotification[1]
            date = pendingNotification[2].strftime('%B %d, %Y')
            notificationID = pendingNotification[3]
            sortDate = pendingNotification[2].strftime('%Y%m%d')
            destination = pendingNotification[4]

            pending.append({
                "id": notificationID,
                "receiver": receiver,
                "message": message,
                "date": date,
                "sortDate": sortDate,
                "destination": destination
            })

        pending = sorted(pending, key=lambda k: k['sortDate'])
        dbConnection.close()
        return pending

    @classmethod
    def findDelivered(cls, id):
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        query = "select receiver, message, date, n.id as notificationID, destination from notifications n join delivered d on n.id = d.id and sender = %s"
        cursor.execute(query, (str(id),))

        result = cursor.fetchall()

        delivered = []
        for deliveredNotification in result:
            receiver = deliveredNotification[0]
            message = deliveredNotification[1]
            date = deliveredNotification[2].strftime('%B %d, %Y')
            notificationID = deliveredNotification[3]
            sortDate = deliveredNotification[2].strftime('%Y%m%d')
            destination = deliveredNotification[4]

            delivered.append({
                "id": notificationID,
                "receiver": receiver,
                "message": message,
                "date": date,
                "sortDate": sortDate,
                "destination": destination
            })
        delivered = sorted(delivered, key=lambda k: k['sortDate'])
        dbConnection.close()
        return delivered

    @classmethod
    def addAPNSToken(cls, id, token):
        try:
            dbConnection = DatabaseConnection.getDBCursor()
            cursor = dbConnection.cursor()

            query = "update users set apnstoken = %s where id = %s"
            cursor.execute(query, (token, id))

            dbConnection.close()
            return {"message": "token added"}, 200
        except:
            return {"message": "an error occured"}, 500
