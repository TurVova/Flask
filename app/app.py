from flask import Flask, request

app = Flask(__name__)

from app import views


app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/gen-pass/<int:pass_len>/<int:pass_count>', 'gen_pass', views.gen_pass)
# app.add_url_rule('/all-customers', views.exec_query)
