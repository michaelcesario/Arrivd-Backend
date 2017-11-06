from flask_restful import Resource, reqparse
from apns import APNs, Frame, Payload
import os

class Test(Resource):
    def get(self):


        cert = os.environ['arrivd-dev-cert']
        key = os.environ['arrivd-dev-key']

        certFile = open('certFile.pem', "w+")
        certFile.write(cert)
        certFile.close()

        keyFile = open('keyFile.pem', "w+")
        keyFile.write(key)
        keyFile.close()

        #certFile = open('certFile.pem', "r")
        #keyFile = open('keyFile.pem', "r")

        #print('HELLO THERE')
        #print(certFile.name)

        apns = APNs(use_sandbox=True, cert_file='certFile.pem', key_file='keyFile.pem')

        # Send a notification
        token_hex = '72DDC06B5E4CA9A2AF5C8F1A52D565867BE5CA0C107CDE12050F184BF28313C3'
        payload = Payload(alert="Hello World!", sound="default", badge=1)
        apns.gateway_server.send_notification(token_hex, payload)

        #certFile.close()
        #keyFile.close()

        return {"message": "hi"}