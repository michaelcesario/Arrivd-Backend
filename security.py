from werkzeug.security import safe_str_cmp
from Models.UserModel import UserModel
from passlib.hash import sha256_crypt

def authenticate(username, password):
    user = UserModel.findByUsername(username)

    if not user:
        return None

    if sha256_crypt.verify(str(password), str(user.password)):
        return user
    else:
        return None

# JWT function: payload contains info in jwt
def identity(payload):
    userID = payload['identity']
    return UserModel.findByID(userID)