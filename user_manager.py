from message_script import User
from message_script.dbhandler import connect_to_db, close_connection
from bcrypt import hashpw, gensalt
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
                        action="store", dest="new_pass",
                        help="Updated password")
    parser.add_argument("-l", "--list",
                        action="store_true", dest="list", default=False,
                        help="List request")
    parser.add_argument("-d", "--delete",
                        action="store_true", dest="delete", default=False,
                        help="Cinema name")
    parser.add_argument("-e", "--email",
                        action="store", dest="email",
                        help="User email")
    options = parser.parse_args()
    return options

def user_manager(options):

    def validate_user(cursor, options):
        password_attempt = options.password
        hashed_password = ''
        if hashpw(password_attempt, hashed_password) == hashed_password:
            pass

    def delete_user(cursor, options):

        print('deleting')
        print(options.username, options.password)

    def add_user(cursor, options):
        pass

    def update_password(cursor, options):
        pass

    def list_users(cursor, options):
        print('listing users')

    cnx, cursor = connect_to_db()
    print(options)

    if (options.delete and options.username and options.password and
            not any([options.list, options.new_pass])):
        delete_user(cursor, options)

    if (options.list and
        not any([options.delete,
                options.username,
                options.password,
                options.new_pass])):
        list_users(cursor, options)

    close_connection(cnx, cursor)


if __name__ == '__main__':
    user_manager(set_options())
