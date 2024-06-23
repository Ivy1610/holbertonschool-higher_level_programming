#!/usr/bin/python3
"""
    Script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


def connectDb(username, password, database, state_name):
    """
    Connects to MySQL database

    Agrs:
        username (str): Username of the user
        password (str): Password of the user
        database (str): Database name
        state_name (str): State name to search for

    Returns:
        database connection
    """
    try:
        connect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )
        return connect

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    connect = connectDb(username, password, database, state_name)

    try:
        curs = connect.cursor()
        query = """
            SELECT *
            FROM states
            WHERE states.name = '{}'
            ORDER BY id ASC".format(state_name)
            """
        curs.execute(query)
        query_rows = curs.fetchall()

        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error executing SQL query: {e}")

    finally:
        curs.close()
        connect.close()
