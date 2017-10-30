from werkzeug.security import safe_str_cmp
from Models.UserModel import UserModel


def authenticate(username, password):
    user = UserModel.findByUsername(username)
    if safe_str_cmp(user.password, password):
        return user
    else:
        return None


# JWT function: payload contains info in jwt
def identity(payload):
    userID = payload['identity']
    return UserModel.findByID(userID)
