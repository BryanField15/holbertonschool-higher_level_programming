#!/usr/bin/python3
"""
Takes in an argument and displays all values matching the argument
and is injection proof.
"""

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

    query = "SELECT * FROM states WHERE BINARY name \
        LIKE %s ORDER BY id;"
    name = (sys.argv[4] + '%',)

    cur = db.cursor()
    cur.execute(query, name)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
