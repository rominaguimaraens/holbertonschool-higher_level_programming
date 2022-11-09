#!/usr/bin/python3
"""Python interpreter"""
import MySQLdb
from sys import argv


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
    cursor.execute('''SELECT * FROM states WHERE name LIKE %s
    ORDER BY states.id ASC;'''.format(argv[4]))
    result = cursor.fetchall()

    for row in result:
        if row[1] == argv[4]:
            print(row)
