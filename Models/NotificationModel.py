#from twilio.rest import Client
import datetime
from apns import APNs, Frame, Payload
from db import DatabaseConnection
import os

# Channel:
#   1 = text message
#   2 = push notification (if applicable)
#   3 = text message + push notification

class NotificationModel:
    def __init__(self, sender, receiver, message, channel, destination):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.channel = channel
        self.destination = destination

    def saveNotification(self):

        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        query = "insert into notifications(sender, receiver, message, channel, destination) values (%s, %s, %s, %s, %s); select currval('notifications_id_seq')"
        cursor.execute(query, (int(self.sender), self.receiver, self.message, self.channel, self.destination))
        result = cursor.fetchone()

        dbConnection.commit()
        notificationID = int(result[0])

        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month) if now.month >= 10 else ('0' + str(now.month))
        day = str(now.day) if now.day >= 10 else ('0' + str(now.day))
        date = year + '-' + month + '-' + day

        query = "insert into pending(id, date) values (%s, (to_date(%s, 'YYYY-MM-DD')))"
        cursor.execute(query, (notificationID, date))

        dbConnection.commit()
        dbConnection.close()
        return notificationID


    def sendNotification(self, token):
        cert = os.environ['arrivd-dev-cert']
        key = os.environ['arrivd-dev-key']

        certFile = open('certFile.pem', "w+")
        certFile.write(cert)
        certFile.close()

        keyFile = open('keyFile.pem', "w+")
        keyFile.write(key)
        keyFile.close()

        # certFile = open('certFile.pem', "r")
        # keyFile = open('keyFile.pem', "r")

        apns = APNs(use_sandbox=True, cert_file='certFile.pem', key_file='keyFile.pem')

        # Send a notification
        token_hex = token
        payload = Payload(alert=self.message, sound="default", badge=0)
        apns.gateway_server.send_notification(token_hex, payload)

        # certFile.close()
        # keyFile.close()

    @classmethod
    def deleteFromPending(cls, id):
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        query = "delete from pending where id = %s"
        cursor.execute(query, (id,))

        dbConnection.commit()
        dbConnection.close()


    @classmethod
    def postToDelivered(cls, id):
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month) if now.month >= 10 else ('0' + str(now.month))
        day = str(now.day) if now.day >= 10 else ('0' + str(now.day))
        date = year + '-' + month + '-' + day

        query = "insert into delivered(id, date) values (%s, (to_date(%s, 'YYYY-MM-DD')))"
        cursor.execute(query, (id, date))

        dbConnection.commit()
        dbConnection.close()

    @classmethod
    def removePending(self, id):

        pass