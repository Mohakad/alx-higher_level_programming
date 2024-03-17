#!/usr/bin/python3
"""script that lists all cities"""
import MySQLdb
import sys


if __name__ == "__main__":
    with MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306) as db:
        crr = db.cursor()
        crr.execute("""SELECT cities.name FROM
                    cities INNER JOIN states ON states.id=cities.state_id
                    WHERE states.name=%s""", (sys.argv[4],))
        rows = crr.fetchall()
        city = [row[0] for row in rows]

        print(*city, sep=", ")
        crr.close()
