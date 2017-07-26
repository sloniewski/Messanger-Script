from message_script.classes import Message, User
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
                        action="store", dest="to", default=False,
                        help="Message recipient id")
    parser.add_argument("-s", "--send",
                        action="store", dest="content", default=False,
                        help="Message text")
    options = parser.parse_args()
    return options

def message_manager(options):
    cnx, cursor = connect_to_db()

    if not all([options.username, options.password]):
        print('You have to provide username and password')
        return

    user = User()
    if not user.authenticate(cursor, options.username, options.password):
        print('Invalid username or password')
        return

    if (options.list and not any([options.to, options.content])):
        print('Listing messages for: {0}'.format(options.username))
        Message.list_all(cursor, user.user_id)

    if (all([options.content, options.to]) and not options.list):
        message = Message(options.content, options.to, user.user_id)
        message.send(cursor)

    close_connection(cnx, cursor)


if __name__ == '__main__':
    message_manager(set_options())
