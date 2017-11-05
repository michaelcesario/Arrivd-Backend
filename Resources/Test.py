from flask_restful import Resource, reqparse
from apns import APNs, Frame, Payload


class Test(Resource):
    def get(self):
        apns = APNs(use_sandbox=True, cert_file='/Users/michaelcesario/git/Arrivd-Backend/arrivd-dev-cert.pem', key_file='/Users/michaelcesario/git/Arrivd-Backend/arrivd-dev-key-noenc.pem')

        # Send a notification
        token_hex = '72DDC06B5E4CA9A2AF5C8F1A52D565867BE5CA0C107CDE12050F184BF28313C3'
        payload = Payload(alert="Hello World!", sound="default", badge=1)
        apns.gateway_server.send_notification(token_hex, payload)
        return {"message": "hi"}