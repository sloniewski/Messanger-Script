from message_script import User
from message_script.dbandler import connect_to_db, close_connection
import argparse


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username",
                        action="store", dest="username",
                        help="User name")
    parser.add_argument("-p", "--password",
                        action="store", dest="password",
                        help="User password")
    parser.add_argument("-n", "--new-pass",
                        action="store", dest="new-pass",
                        help="Updated password")
    parser.add_argument("-l", "--list",
                        action="store_true", dest="list", default=False,
                        help="List request")
    parser.add_argument("-d", "--delete",
                        action="store_true", dest="delete", default=False,
                        help="Cinema name")
    parser.add_argument("-e", "--edit",
                        action="store", dest="email",
                        help="User email for edit")
    options = parser.parse_args()
    return options


if __name__ == '__main__':
    cnx, cursor = connect_to_db()

    users = User.load_all_users(cursor)
    for user in users:
        print(user)
    close_connection(cnx, cursor)
