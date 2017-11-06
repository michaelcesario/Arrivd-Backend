from flask_restful import Resource, reqparse
from Models.NotificationModel import NotificationModel
from Models.UserModel import UserModel


class Pending(Resource):

    def get(self, id):
        return UserModel.findPending(int(id))


    def delete(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True)

        notificationID = (parser.parse_args())['id']
        print(notificationID)
        NotificationModel.deleteFromPending(notificationID)

