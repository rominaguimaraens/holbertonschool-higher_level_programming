#!/usr/bin/python3
"""Python interpreter"""
from sys import argv

import MySQLdb

"""sql query"""
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
        )

    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities JOIN states 
    ON cities.state_id = states.id AND states.name = %S
    ORDER BY cities.id ASC""", (argv[4], ))
    result = cursor.fetchall()

    for row in result:
        print(row)
