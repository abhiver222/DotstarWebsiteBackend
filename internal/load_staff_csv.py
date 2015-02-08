'''
adds (real) data for students into the proper tables from a csv
'''
import sys,pymysql,csv
from config import *

def build_query(data,stub):
    res='{0} VALUES ('.format(stub)
    for i in range(len(data)):
        res+="{0}, ".format(conn.escape(data[i]))
    return '{0});'.format(res[:-2])


if len(sys.argv) < 2:
    print("please rerun, including the filename as an argument (e.g. python load_csv.py staff.csv)\n\n")
    sys.exit(0)


conn = pymysql.connect(host=DB_HOST,port=DB_PORT,user=DB_USER,passwd=DB_PASSWORD, db=DB_NAME)
cur = conn.cursor()
with open(sys.argv[1]) as students:
    reader = csv.DictReader(students)
    for row in reader:
        if len(row['Netid']) < 1:
            continue;
        user = [
            row['Netid'],
            row['UIN']
        ]

        user_details = [
            row['Netid'],
            row['First'],
            row['Last'],
            row['Prefered Email'],
            row['Major']
        ]

        queries = [build_query(user, 'INSERT INTO Users (NetId, UIN)'), build_query(user_details,'INSERT INTO UserDetails (NetId, FirstName, LastName, BestEmail, Major)')]
        map(cur.execute, queries)
        conn.commit()
