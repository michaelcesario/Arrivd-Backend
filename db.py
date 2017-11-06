import psycopg2
import os
from urllib.parse import urlparse


class DatabaseConnection:
    @classmethod
    def getDBCursor(cls):
        url = urlparse(os.environ['DATABASE_URL'])
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port

        dbConnection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return dbConnection
