import mysql.connector
from mysql.connector import Error


def connect():
    """ Connecting to MySQL database """
    conn = None
    try:
        #Information intentially left out
        conn = mysql.connector.connect(host='[]',
                                       database='[]',
                                       user='[]',
                                       password='[]')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()
