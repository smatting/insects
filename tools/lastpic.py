import sqlite3
import sys

def get_last(filename):
    '''
    load frames out of a Motion sqlite3 database
    '''
    with sqlite3.connect(filename) as conn:
        sql = 'select filename from security order by time_stamp desc limit 1'
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchone()[0]

def main(filename):
    print(get_last(filename))


if __name__ == '__main__':
    main(sys.argv[1])
