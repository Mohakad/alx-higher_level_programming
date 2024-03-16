#!/usr/bin/python3
""" lists all states from database"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
    passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cr = db.cursor()
    cr.execute("SELECT * FROM states")
    dat = cr.fetchall()
    for data in dat:
        print(data)
    cr.close()
    db.close()
