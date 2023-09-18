#!/usr/bin/python3
'''
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
'''

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE cities.state_id\
                = (SELECT id FROM states WHERE name = %s)\
                ORDER BY cities.id ASC", [sys.argv[4]])
    data = cur.fetchall()
    print(", ".join([name[0] for name in data]))
    cur.close()
    db.close()
