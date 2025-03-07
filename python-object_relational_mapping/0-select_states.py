#!/usr/bin/env python3

import MySQLdb
import sys


def main():

    # Get MySQL credentials from command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=mysql_db
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
