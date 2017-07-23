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
    parser.add_argument("-e", "--edit",
                        action="store_true", dest="edit", default=False,
                        help="Edit password")
    options = parser.parse_args()
    return options


def user_manager(options):

    def delete_user(cursor, options):
        user_to_del = User()
        if user_to_del.validate(cursor, options.username, options.password):
            user_to_del.del_user(cursor)
            del(user_to_del)
            print('Removed user: {0}'.format(options.username))
        else:
            print('User: {0}, not found or wrong passowrd'.format(options.username))

    def add_user(cursor, options):
        new_user = User()
        new_user.username = options.username
        new_user.set_password(options.password)
        new_user.save_to_db(cursor)
        print('Added user: {0}'.format(options.username))

    def update_password(cursor, options):
        user_to_mod = User()
        if user_to_mod.validate(cursor, options.username, options.password):
            user_to_mod.set_password(options.new_pass)
            user_to_mod.update_pass(cursor)
            print('Updated passowrd for user: {0}'.format(options.username))
        else:
            print('User: {0}, not found or wrong passowrd'.format(options.username))

    def list_users(cursor, options):
        users = User.load_all_users(cursor)
        for user in users:
            print(user)

    cnx, cursor = connect_to_db()
    print(options)
    flag = 0
    if(all([options.new_pass, options.edit, options.username, options.password])
            and not any([options.list, options.delete])):
        update_password(cursor, options)
        flag = 1

    if (all([options.delete, options.username, options.password]) and
            not any([options.list, options.new_pass, options.edit])):
        delete_user(cursor, options)
        flag = 1

    if (options.list and
        not any([options.delete, options.username, options.edit,
                options.password, options.new_pass])):
        list_users(cursor, options)
        flag = 1

    if (options.username and options.password and
        not any([options.delete, options.list,
                 options.new_pass, options.edit])):
        add_user(cursor, options)
        flag = 1

    if (flag==0): print('Use --help for more information')

    close_connection(cnx, cursor)


if __name__ == '__main__':
    user_manager(set_options())
