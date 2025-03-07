#!/usr/bin/env python3
"""
This script lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The MySQL username.
    mysql_password: The MySQL password.
    database_name: The name of the database to connect to.

The script connects to a MySQL server running on localhost at port 3306,
executes a query to retrieve all states sorted by id in ascending order,
and prints each state.
"""

import MySQLdb
import sys

def main():
    """
    Main function that retrieves and prints all states from the database.
    """
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
