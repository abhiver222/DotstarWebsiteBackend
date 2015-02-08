from flask import current_app
import pymysql as sql
from functools import partial


def to_dict(cur, row):
    '''
    turn a row into a dictionary, keys of which are column names
    '''
    columns = map(lambda col_desc: col_desc[0], cur.description)
    return {columns[i].lower(): row[i] for i in xrange(len(row))}


def get_one(cur):
    '''
    get a single row from cursor
    '''
    row = cur.fetchone()
    return to_dict(cur, row)

def get_all(cur):
    '''
    get rows from cursor
    '''
    return map(partial(todict, cur), cur.fetchall())


def get_cursor():
    '''
    usage:
    cur = get_cursor()
    cur.execute([your statement])
    # cur.fetchone() for a single row
    # cur.fetchall() returns a iterator of fetched rows
    for row in cur.fetchall():
        ... do stuff here ...
    '''
    conn = sql.connect(**current_app.db_config)
    return conn.cursor(), conn


def verify_user(netid, uin):
    '''
    verify if a user with given netid and uin exists
    '''
    cur, _ = get_cursor()
    cur.execute('''
        SELECT *
        FROM Users
        WHERE
        NetId = %s AND
        UIN = %s;''', (netid, uin,))
    user_row = cur.fetchone()
    return user_row is not None 



def update_user_details(year,email,github,euler,phone,experience,goals,netid):
    '''
    a user wants to modify their information
    note that all user-editable fields will be updated,
    since the form was already prepopulated with all old values
    '''
    cur, conn = get_cursor()
    cur.execute('''
        UPDATE UserDetails
        SET Phone = %s,
            BestEmail = %s,
            Github = %s,
            Euler = %s,
            Year = %s,
            Skills = %s,
            Wants = %s
        WHERE NetId = %s;''', (phone,email,github,euler,year,experience,goals,netid,))
    conn.commit()


def get_user_details(netid):
    cur, _ = get_cursor()
    cur.execute('''
    SELECT * FROM UserDetails
    WHERE
    NetID = %s;''', netid)
    return get_one(cur)
