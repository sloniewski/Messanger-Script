from message_script import Message, User
from message_script.dbhandler import connect_to_db, close_connection
import argparse


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username",
                        action="store", dest="username",
                        help="User name")
    parser.add_argument("-p", "--password",
                        action="store", dest="password",
                        help="User password")
    parser.add_argument("-l", "--list",
                        action="store_true", dest="list", default=False,
                        help="List messages")
    parser.add_argument("-t", "--to",
                        action="store_true", dest="to", default=False,
                        help="Message recipient id")
    parser.add_argument("-s", "--send",
                        action="store", dest="send", default=False,
                        help="Message text")
    options = parser.parse_args()
    return options

def message_manager(options):
    if not all([options.username, options.password]):
        print('You have to give username and password')
        return

    user = User()
    if not user.validate(cursor, options.username, options.password):
        print('Invalid username or password')
        return

    def send(cursor, options, User):
        """
        check if recipient exits and send message
        """
        pass

    def list(cursor, User):
        """
        Lists all messages for User
        """
        pass

    cnx, cursor = connect_to_db()

    if (options.list and not any([options.to, options.send])):
        list(cursor, User)

    if (all([options.send, options.to]) and not options.list):
        send(cursor, options, User)

    close_connection(cnx, cursor)


if __name__ == '__main__':
    message_manager(set_options())
