from flask_restful import Resource
from Models.UserModel import UserModel

class Delivered(Resource):

    def get(self, id):
        return UserModel.findDelivered(int(id))
