from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dbdir/test.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<ID: {},User: {}, Email: {}>'.format(self.id,
                                                     self.username,
                                                     self.email
                                                )

# db.drop_all()
# db.create_all()

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')


# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()
#
#
User.query.all()
#
User.query.filter_by(username='admin').first()




# import datetime
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# app.config['SQLALCHEMY_ECHO'] = True
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     created = db.Column(db.DateTime, default=datetime.datetime.now)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User ID: {}, NAME: {}, Email: {}, DATE: {}>'.format(
#         	self.id,
#         	self.username,
#         	self.email,
#         	self.created
#         )
#
# db.drop_all()
# db.create_all()
#
#
# user = User("Dima", "example@gmail.com")
# print(user.id)
# print(user.username)
# print(user.email)
#
# db.session.add(user)
# db.session.commit()


# users =

# db.drop_all()
# db.create_all()
#
# for i in range(100):
#     # user = User("NAME {}".format(i), "example_{}gmail.com".format(i))

# db.session.add(user)
# db.session.commit()

# user = User.query
# print(user.count())
