class Message():
    def __init__(self, text, sender_id, recipient_id):
        self.text = text
        self.sender_id = sender_id
        self.recipient_id = recipient_id

    def list_all(self):
        pass

    def send(self):
        pass

    def delete(self):
        pass


class User():
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
        self.user_id = -1

    def save_to_db(self):
        pass

    def update_pass(self):
        pass

    def list_users(self):
        pass

    def del_user(self, user_id):
        pass
