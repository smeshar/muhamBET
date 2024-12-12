import functions
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

    def register(self, name: str, password: str, key: str) -> list:
        self.connect()
        self.cursor.execute(f"SELECT * FROM gamekeys")

        rows = self.cursor.fetchall()
        f = False
        for i in rows:
            f |= (i[0] == key)

        if not f:
            print(" Несуществующий ключ к игре")
            return []

        self.cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")

        rows = self.cursor.fetchall()

        if len(rows) == 0:
            print(" Несуществующий пользователь")
            return []

        passw = rows[0][2]
        if passw != password:
            print(" Неверный пароль")
            return []

        self.cursor.execute(f"DELETE FROM gamekeys WHERE gamekey = '{key}'")
        self.cursor.execute(f"insert into users_muhambet values ({rows[0][0]})")

        self.close()
        return rows[0]

    def login(self, name, password) -> list:
        self.connect()
        self.cursor.execute(f"SELECT id, password FROM users WHERE name = '{name}'")
        rows = self.cursor.fetchone()

        if password != rows[1]:
            print(" Неверный пароль")
            return []

        self.cursor.execute(f"SELECT * FROM users_muhambet WHERE id = '{rows[0]}'")
        rows = self.cursor.fetchone()
        if rows is None:
            print(" Пользователь не зарегистрирован")

        self.cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
        return self.cursor.fetchall()[0]

    def get_balance(self) -> float:
        return 0.0

    def get_teams(self) -> list:
        return [functions.get_team(), functions.get_team()]

    def get_coefs(self) -> list:
        return [1, 2]

    def get_time(self) -> int:
        return 322

    def top_players(self) -> list:
        return ["simple"]

    def get_all(self) -> list:
        return [self.get_balance(), self.get_teams(), self.get_coefs(), self.get_time(), self.top_players()]
