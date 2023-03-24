#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Database connection arguments
    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Connect to MySQL database
    db_conn = MySQLdb.connect(host=host, port=port, user=user,
                              passwd=passwd, db=db)

    # Create cursor to execute queries
    cursor = db_conn.cursor()

    # Execute query to fetch all states from the table states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db_conn.close()

