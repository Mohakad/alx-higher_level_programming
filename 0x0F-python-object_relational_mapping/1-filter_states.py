#!/usr/bin/python3
"""starting with N (upper N) from the database"""
import sys
import MySQLdb


if __name__ == "__main__":
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], port=3306)
    crr = dtb.cursor()
    crr.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    dat = crr.fetchall()
    for d in dat:
        print(d)
    crr.close()
    dtb.close()
