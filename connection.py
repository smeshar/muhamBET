import pymysql
import passwords

class Conn():
    def connect(self):
        self.connection = pymysql.connect(host=passwords.hostname, port=passwords.port, database=passwords.database,
                                          user=passwords.username, password=passwords.password)
        self.connection.connect()
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def register(self, name: str, password: str, key: str):
        self.connect()

        query = f"SELECT * FROM gamekeys"
        self.cursor.execute(query)

        rows = self.cursor.fetchall()
        f = False
        for i in rows:
            print(i)
            f |= (i[0] == key)

        if not f:
            print(" Несуществующий ключ к игре")
            return []

        query = f"SELECT * FROM users WHERE name = '{name}'"
        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        if len(rows) == 0:
            print(" Несуществующий пользователь")
            return []

        passw = rows[0][2]
        if passw != password:
            print(" Неверный пароль")
            return []

        query = f"DELETE FROM gamekeys WHERE gamekey = '{key}'"
        self.cursor.execute(query)

        query = f"insert into users_muhambet values ({rows[0][0]})"
        self.cursor.execute(query)

        self.close()
        return rows[0]