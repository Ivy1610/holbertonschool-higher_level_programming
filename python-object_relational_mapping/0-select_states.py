#!/usr/bin/python3
"""
Script that lists all states from the database
"""
import MySQLdb
import sys


def connectDb(username, password, database):
    """
        Get connection with the database .
        Args:
            username (str): Username of the user
            password (str): Password of the user
            database (str): Database to retrieve
        Return:
            Connection database
    """
    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    return connect


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connect = connectDb(username, password, database)
    curs = connect.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = curs.fetchall()

    for row in query_rows:
        print(row)
    curs.close()
    connect.close()
