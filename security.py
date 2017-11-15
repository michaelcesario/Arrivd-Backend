from werkzeug.security import safe_str_cmp
from Models.UserModel import UserModel
from passlib.hash import sha256_crypt

def authenticate(username, password):
    userByName = UserModel.findByUsername(username)
    userByNumber = UserModel.findByPhoneNumber(username)

    if not (userByName or userByNumber):
        return None

    if userByName:
        if sha256_crypt.verify(str(password), str(userByName.password)):
            return userByName
    elif userByNumber:
        if sha256_crypt.verify(str(password), str(userByNumber.password)):
            return userByNumber
    else:
        return None

# JWT function: payload contains info in jwt
def identity(payload):
    userID = payload['identity']
    return UserModel.findByID(userID)