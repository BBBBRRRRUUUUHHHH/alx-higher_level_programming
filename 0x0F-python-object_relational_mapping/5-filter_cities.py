#!/usr/bin/python3
import MySQLdb
import sys
"""
Write a script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":

    db_host = "localhost"
    db_user = sys.argv[1]  # "your_username"
    db_password = sys.argv[2]  # "your_password"
    db_name = sys.argv[3]  # "your_database_name"
    port = 3306
    state_name = sys.argv[4]  # "your_database_name"
    query = "SELECT name FROM cities WHERE state_id = \
(SELECT id FROM states WHERE name LIKE BINARY %s) ORDER BY cities.id ASC"
    params = (state_name,)
    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2]for ct in cursor.fetchall()if ct[4] == sys.argv[4]]))
