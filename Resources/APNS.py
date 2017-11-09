from flask_restful import Resource, reqparse
from Models.UserModel import UserModel

class APNS(Resource):

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, required=True)

        token = (parser.parse_args())['token']
        return UserModel.addAPNSToken(id, token)
