#!/usr/bin/python3
"""0-select_states module"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,  # default anyway
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
