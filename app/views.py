from flask import render_template, request
from app.utils import id_generator
from app.utils import all_customers
from app.utils import customer_id
from app.utils import customers_country
from app.utils import phones_search
from app.utils import filter_db

def index():
    return render_template('index.html')

def gen_pass(pass_len, pass_count):
    context = {
        "passwords": [id_generator(pass_len) for i in range(pass_count)],
        "pass_len": pass_len,
        "pass_count": pass_count,
    }
    return render_template('passwords.html', context=context)

def customers():
    context = all_customers()
    return render_template("customers.html", context=context)

def id_customer(customerid):
    context = customer_id(customerid)
    return render_template("customers.html", context=context)

def country_customers(country):
    context = customers_country(country)
    return render_template("customers.html", context=context)

def search_phone(phone):
    phone = request.args.get('phone')
    context = phones_search(phone)
    return render_template("customers.html", context=context)

def db_filter():
    country = request.args.get('country')
    state = request.args.get('state')
    city = request.args.get('city')
    '''params = {
        'Country' : country
        'State' : state
        'City' : city
    }'''
    context = filter_db(country, state, city)
    return render_template('customers.html', context=context)