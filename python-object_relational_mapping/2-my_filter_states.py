#!/usr/bin/python3

import MySQLdb
import sys

"""script that takes in an argument and displays all values in the states"""
"""table of hbtn_0e_0_usa where name matches the argument."""


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

    name = sys.argv[4]
    query = "SELECT * FROM states WHERE BINARY name \
        LIKE '{}%' ORDER BY id;" .format(name)

    cur = db.cursor()
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
