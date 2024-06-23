#!/usr/bin/python3
import MySQLdb
import sys


def connectDb(username, password, database):
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
