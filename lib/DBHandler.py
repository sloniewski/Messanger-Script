from mysql.connector import connect

"""
CREATE TABLE users (
    id int AUTO_INCREMENT,
    email varchar(255) UNIQUE,
    username varchar(255),
    hashed_password varchar(255),
    PRIMARY KEY(id)
);

CREATE TABLE message(
    id INT AUTO_INCREMENT,
    sender_id INT NOT NULL,
    recipient_id INT NOT NULL,
    content TEXT,
    PRIMARY KEY(id),
    FOREIGN KEY(sender_id) REFERENCES users(id),
    FOREIGN KEY(recipient_id) REFERENCES users(id)
);
"""


def connect_to_db():
    cnx = connect(
        user='root',
        password='coderslab',
        database='communicator_db'
    )
    cursor = cnx.cursor()

    return (cnx, cursor)


def close_connection(cnx, cursor):
    cnx.commit()
    cursor.close()
    cnx.close()
