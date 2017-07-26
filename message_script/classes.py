from bcrypt import hashpw, gensalt


class Message:
    """
    Represents message in database
    """

    def __init__(self, text, sender_id, recipient_id):
        self.text = text
        self.sender_id = sender_id
        self.recipient_id = recipient_id

    def send(self, cursor):
        sql = 'INSERT INTO message(sender_id, recipient_id, content)  \
              VALUES (%s, %s, %s)'
        cursor.execute(sql, (self.sender_id, self.recipient_id, self.text))
        print('{0} message send to id: {1}'.format(cursor.rowcount, self.recipient_id))

    @staticmethod
    def list_all(cursor, user_id):
        sql = 'SELECT * FROM message WHERE recipient_id=%s'
        cursor.execute(sql, (user_id,))
        print(cursor.statement)
        for record in cursor:
            print(record)

    @staticmethod
    def delete(cursor, message_id):
        sql = 'DELETE FROM message WHERE id=%s'
        cursor.execute(sql)
        print('Deleted {0} messages'.format(cursor.rowcount))
        return

    def __str__(self):
        return 'Send to {0}, content: {1}'.format(self.recipient_id, self.text)


class User:
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
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    def set_password(self, password):
        self.__hashed_password = hashpw(password.encode(), gensalt(10))

    def save_to_db(self, cursor):
        if self.__id == -1:
            sql = 'INSERT INTO users(email, username, hashed_password)\
                   VALUES (%s, %s, %s)'
            params = (self.email, self.username, self.hashed_password)
            cursor.execute(sql, params)
            return True
        return False

    def authenticate(self, cursor, username, password_attempt):
        sql = 'SELECT * FROM users WHERE username=%s LIMIT 1'
        cursor.execute(sql, (username,))
        data = cursor.fetchone()
        if data is not None:
            self.__hashed_password = data[3]
        if hashpw(password_attempt.encode(), self.hashed_password.encode()) == self.hashed_password.encode():
            self.__id = data[0]
            self.email = data[1]
            return True
        self.__hashed_password = ''
        return False

    @staticmethod
    def load_user_by_id(cursor, user_id):
        sql = 'SELECT * FROM users where id = %s'
        params = (user_id,)
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

    def update_pass(self, cursor):
        sql = 'UPDATE users SET hashed_password=%s WHERE id=%s;'
        params = (self.hashed_password, self.__id)
        cursor.execute(sql, params)
        print(cursor.statement)
        return True

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

    def del_user(self, cursor):
        sql = 'DELETE FROM users WHERE id=%s'
        cursor.execute(sql,	(self.__id,))
        self.__id = -1
        return True

    def __str__(self):
        return 'User: {0}, id: {1}'.format(self.username, str(self.__id))
