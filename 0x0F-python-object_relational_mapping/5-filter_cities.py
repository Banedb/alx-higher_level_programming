#!/usr/bin/python3
"""5-filter_cities module"""

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
    cur.execute("""
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """, (argv[4],))

    print(", ".join(row[0] for row in cur.fetchall()))

    cur.close()
    db.close()
