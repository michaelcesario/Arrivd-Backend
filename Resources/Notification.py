from flask_restful import Resource, reqparse
from Models.NotificationModel import NotificationModel

class Notification(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('sender', type=str, required=True)
        parser.add_argument('receiver', type=str, required=True)
        parser.add_argument('message', type=str, required=True)
        parser.add_argument('channel', type=str, required=True)

        notificationData = parser.parse_args()

        notification = NotificationModel(
            notificationData['sender'],
            notificationData['receiver'],
            notificationData['message'],
            notificationData['channel']
        )

        id = notification.saveNotification()
        return {"notificationid": id}