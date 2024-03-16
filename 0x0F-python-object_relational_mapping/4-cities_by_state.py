#!/usr/bin/python3
"""starting with N (upper N) from the database"""
import sys
import MySQLdb


if __name__ == "__main__":
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], port=3306)
    crr = dtb.cursor()
    crr.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    dat = crr.fetchall()
    for d in dat:
        print(d)
    crr.close()
    dtb.close()
