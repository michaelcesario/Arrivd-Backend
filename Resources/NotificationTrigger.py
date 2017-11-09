from flask_restful import Resource, reqparse
from Models.NotificationModel import NotificationModel
from db import DatabaseConnection

class NotificationTrigger(Resource):

    def post(self, id):

        try:
            # Get notification from database and send
            dbConnection = DatabaseConnection.getDBCursor()
            cursor = dbConnection.cursor()

            query = "select id, sender, receiver, message, channel, destination from notifications where id = %s"
            cursor.execute(query, (id,))
            notificationData = cursor.fetchone()

            query = "select username, phonenumber, apnstoken from users where id = %s"
            cursor.execute(query, (int(notificationData[1]),))
            sender = cursor.fetchone()[0]

            query = "select apnstoken from users where username = %s"
            cursor.execute(query, (notificationData[2],))
            receiverToken = cursor.fetchone()[0]

            dbConnection.close()

            notification = NotificationModel(sender[0], notificationData[2], notificationData[3], notificationData[4], notificationData[5])
            notification.sendNotification(receiverToken)

            NotificationModel.deleteFromPending(id)
            NotificationModel.postToDelivered(id)

            return {"message": "message sent!"}, 200

        except Exception as e:

            return {"error": e}, 500
