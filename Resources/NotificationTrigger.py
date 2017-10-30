from flask_restful import Resource, reqparse
from Models.NotificationModel import NotificationModel
import psycopg2
import constants


class NotificationTrigger(Resource):

    def post(self, id):

        # Get notification from database and send
        dbConnection = psycopg2.connect(database=constants.dbName, user=constants.dbUser, password=constants.dbPassword, host=constants.dbHost)
        cursor = dbConnection.cursor()

        query = "select id, sender, receiver, message, channel from notifications where id = %s"
        cursor.execute(query, (id,))
        notificationData = cursor.fetchone()

        query = "select username, phonenumber from users where id = %s"
        cursor.execute(query, (notificationData[0],))
        sender = cursor.fetchone()

        dbConnection.close()

        notification = NotificationModel(sender[0], notificationData[2], notificationData[3], notificationData[4])
        notification.sendNotification()

        return {"message": "message sent!"}