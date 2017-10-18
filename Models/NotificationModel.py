import psycopg2
from Models.UserModel import UserModel
from twilio.rest import Client
import constants

# Channel:
#   1 = text message
#   2 = push notification (if applicable)
#   3 = text message + push notification

class NotificationModel:
    def __init__(self, sender, receiver, message, channel):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.channel = channel

    def saveNotification(self):

        dbConnection = psycopg2.connect(database=constants.dbName, user=constants.dbUser, password=constants.dbPassword, host=constants.dbHost)
        cursor = dbConnection.cursor()

        query = "insert into notifications(sender, receiver, message, channel) values (%s, %s, %s, %s); select currval('notifications_id_seq')"
        cursor.execute(query, (int(self.sender), self.receiver, self.message, self.channel))
        result = cursor.fetchone()

        dbConnection.commit()
        dbConnection.close()

        return int(result[0])

    def sendNotification(self):
        pass
        #client = Client(constants.twilioAccountSID, constants.twilioAuthToken)
        #client.api.account.messages.create(
            #to="+16473803828",
            #from_="+19029070302",
            #body="Hello there!")
