#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
"""
import MySQLdb
import sys

if __name__ == "__main__":

    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=3306
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
