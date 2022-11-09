#!/usr/bin/python3
"""Python interpreter"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost"
        port=3306
        user=argv[1]
        password=argv[2]
        db_name=argv[3]
    )

cursor = db.cursor()
cursor.execute(
    SELECT * FROM 
)