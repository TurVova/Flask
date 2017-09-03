from flask import render_template
# from flask import request
from app.utils import id_generator
# from app.utils import all_customers
# from app.utils import customer_id
# from app.utils import customers_country
# from app.utils import phones_search
# from app.utils import filter_db

def index():
    return render_template('index.html')

def gen_pass(pass_len, pass_count):
    context = {
        "passwords": [id_generator(pass_len) for i in range(pass_count)],
        "pass_len": pass_len,
        "pass_count": pass_count,
    }
    return render_template('passwords.html', context=context)

# def base():
#     return render_template("all_customers.html")
