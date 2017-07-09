from mysql.connector import connect


def connect_to_db():
    cnx = connect(
        user='root',
        password='coderslab',
        database='communicator_db'
    )
    cursor = cnx.cursor()

    return (cnx, connect)


def close_connection(cnx, cursor):
    cursor.close()
