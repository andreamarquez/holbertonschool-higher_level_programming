#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    This version prevents SQL injection
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="127.0.0.1", port=3306,
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
