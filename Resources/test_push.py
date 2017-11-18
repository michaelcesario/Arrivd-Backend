from flask_restful import Resource, reqparse
from apns import APNs, Frame, Payload
from db import DatabaseConnection
import os

class TestPush(Resource):
    def get(self, message):
        cert = os.environ['arrivd-dev-cert']
        key = os.environ['arrivd-dev-key']

        certFile = open('certFile.pem', "w+")
        certFile.write(cert)
        certFile.close()

        keyFile = open('keyFile.pem', "w+")
        keyFile.write(key)
        keyFile.close()

        # certFile = open('certFile.pem', "r")
        # keyFile = open('keyFile.pem', "r")

        apns = APNs(use_sandbox=True, cert_file='certFile.pem', key_file='keyFile.pem')

        # Send a notification
        token_hex = "F7F8D0C3DEFE6F4D6B0FE5C633EB02923D201E9AF7071868BC5A82E14FEE2EB2"
        payload = Payload(alert=message, sound="default", badge=0)
        apns.gateway_server.send_notification(token_hex, payload)
