import psycopg2
#from twilio.rest import Client
import datetime
from db import DatabaseConnection

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

        cursor = DatabaseConnection.getDBCursor()

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

    def sendNotification(self):
        pass
        #client = Client(constants.twilioAccountSID, constants.twilioAuthToken)
        #client.api.account.messages.create(
            #to="+16473803828",
            #from_="+19029070302",
            #body="Hello there!")

    @classmethod
    def deleteFromPending(cls, id):
        cursor = DatabaseConnection.getDBCursor()

        query = "delete from pending where id = %s"
        cursor.execute(query, (id,))

        dbConnection.commit()


    @classmethod
    def postToDelivered(cls, id):
        cursor = DatabaseConnection.getDBCursor()

        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month) if now.month >= 10 else ('0' + str(now.month))
        day = str(now.day) if now.day >= 10 else ('0' + str(now.day))
        date = year + '-' + month + '-' + day

        query = "insert into delivered(id, date) values (%s, (to_date(%s, 'YYYY-MM-DD')))"
        cursor.execute(query, (id, date))

        dbConnection.commit()

    @classmethod
    def removePending(self, id):

        pass