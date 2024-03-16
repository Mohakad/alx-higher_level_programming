#!/usr/bin/python3
""" lists all states from database"""
import sys
import MySQLdb


if __name__ == "__main__":
    ldb = MySQLdb.connect(host="localhost", username=sys.argv[1], password=sys.argv[2],
    ldb=sys.argv[3], port=3306)
    crs = db.cursor()
    crs.execute("SELECT * FROM states")
    dat = crs.fetchall()
    for data in dat:
        print(dat)
        crs.close()
        ldb.close()
