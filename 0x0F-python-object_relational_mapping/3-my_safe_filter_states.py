#!/usr/bin/python3
"""3-my_safe_filter_states module"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (argv[4],))
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
