import string
import random
import sqlite3
import os

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = BASE_DIR + '/chinook.db'

def exec_query(query):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    data = c.execute(query)
    res = list(data)
    conn.commit()
    conn.close()
    return res

def all_customers():
    query = ('SELECT * FROM customers')
    return exec_query(query)

def customer_id(customerid):
    query = ('SELECT * FROM customers WHERE CustomerId = {}'.format(customerid))
    return exec_query(query)

def customers_country(country):
    query = ("SELECT * FROM customers WHERE Country = '{}'".format(country))
    return exec_query(query)

def phones_search(phone):
    query = ("SELECT * FROM customers WHERE Phone LIKE '{}'".format(phone))
    return exec_query(query)

def filter_db(country='%', state='%', city='%'):
    query = "SELECT * FROM customers WHERE Country LIKE '{}' AND State LIKE '{}' AND City LIKE '{}'".format(country, state, city)
    return exec_query(query)


# def exec_query(query):
#     conn = sqlite3.connect('example.db')
#     c = conn.cursor()
#     res = c.execute(query)
#     conn.commit()
#     conn.close()
#     return res
#
# def exec_query(query):
#     conn = sqlite3.connect('chinook.db')
#     c = conn.cursor()
#     res = c.execute("SELECT * FROM customers")
#     rows = res.fetchall()
#     print(res)
#
#     conn.commit()
#     conn.close()
#     return res

# con = sqlite3.connect('chinook.db')
#
# with con:
#     cur = con.cursor()
#     cur.execute("SELECT * FROM customers ")
#     rows = cur.fetchall()
#
#     for row in rows:
#         print(row)

# clipit
if __name__ == '__main__':

    print(list(all_customers()))