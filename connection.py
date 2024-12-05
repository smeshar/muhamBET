import pymysql
import passwords

class Conn():
    def __init__(self):
        self.connection = pymysql.connect(host=passwords.hostname, port=passwords.port, database=passwords.database, user=passwords.user, password=passwords.password)
        self.cursor = self.connection.cursor()

    def connect(self):
        self.connection.connect()

    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def login(self):
        #TODO login system
        pass