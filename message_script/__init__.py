class Message():
    """
    Represents message in database
    """

    def __init__(self, text, sender_id, recipient_id):
        self.text = text
        self.sender_id = sender_id
        self.recipient_id = recipient_id

    def list_all(self):
        cursor = DBHandler.connect_to_db()
        DBHandler.close_connection()

    def send(self):
        pass

    def delete(self):
        pass


class User():
    """
    represents user record in database
    """

    def __init__(self):
        self.username = ''
        self.__hashed_password = ''
        self.email = ''
        self.__id = -1

    @property
    def user_id(self):
        return self._user_id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password, salt):
        # TODO add hashing function
        self.__hashed_password = password + salt

    def save_to_db(self, cursor):
        if self.__id == -1:
            sql = 'INSERT INTO users(email, username, hashed_password)\
                   VALUES (%s, %s, %s)'
            params = (self.email, self.username, self.hashed_password)
            cursor.execute(sql, params)
            return True
        return False

    @staticmethod
    def load_user(cursor, user_id):
        sql = 'SELECT * FROM users where id = %s'
        params = (id,)
        cursor.execute(sql, params)
        data = cursor.fetchone()

        if data is not None:
            u = User()
            u.__id = data[0]
            u.email = data[1]
            u.username = data[2]
            u.__hashed_password = data[3]
            return u
        return None

    def update_pass(self):
        pass

    @staticmethod
    def load_all_users(cursor):
        sql = 'SELECT * FROM users'
        cursor.execute(sql)
        data = cursor.fetchall()

        users = list()
        for user in data:
            u = User()
            u.__id = user[0]
            u.email = user[1]
            u.username = user[2]
            u.__hashed_password = user[3]
            users.append(u)
        return users

    def del_user(self, user_id):
        pass

    def __str__(self):
        return str(self.__id) + ', ' + self.username + ', ' + self.email + ', ' + self.__hashed_password
