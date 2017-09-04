from flask import Flask, request

app = Flask(__name__)

from app import views


app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/gen-pass/<int:pass_len>/<int:pass_count>', 'gen_pass', views.gen_pass)
app.add_url_rule('/customers/', 'customers', views.customers)
app.add_url_rule('/id-customer/<int:customer_id>/', 'id_customer', views.id_customer)
app.add_url_rule('/country-customers/<country>/', 'country', views.country_customers)
app.add_url_rule('/search-phone', 'phone', views.search_phone)
app.add_url_rule('/filter', 'filter', views.db_filter)