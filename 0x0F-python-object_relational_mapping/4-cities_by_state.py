#!/usr/bin/python3
""" script that lists all cities """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    """The execute function requires one parameter, the query."""
    cur.execute("SELECT cities.id, cities.name, states.name\
        FROM cities\
        JOIN states\
        ON cities.state_id=states.id")
    """Obtaining Query Results"""
    rows = cur.fetchall()
    for i in rows:
        print(i)
