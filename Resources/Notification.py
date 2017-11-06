from flask_restful import Resource, reqparse
from Models.NotificationModel import NotificationModel

class Notification(Resource):

    #@jwt_required()
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('sender', type=str, required=True)
        parser.add_argument('receiver', type=str, required=True)
        parser.add_argument('message', type=str, required=True)
        parser.add_argument('channel', type=str, required=True)
        parser.add_argument('destination', type=str, required=True)

        notificationData = parser.parse_args()

        print(notificationData)

        notification = NotificationModel(
            notificationData['sender'],
            notificationData['receiver'],
            notificationData['message'],
            notificationData['channel'],
            notificationData['destination']
        )

        id = notification.saveNotification()
        print("notification id below:")
        print(id)
        return {"notificationid": id}

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True)

        notificationID = (parser.parse_args())['id']
        NotificationModel.deleteFromPending(notificationID)
