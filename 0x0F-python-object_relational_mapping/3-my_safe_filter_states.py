#!/usr/bin/python3
'''
code that is safe from MySQL injections!
'''

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", (sys.argv[4],))
    data = cur.fetchall()
    for DATA in data:
        print(DATA)
    cur.close()
    db.close()
