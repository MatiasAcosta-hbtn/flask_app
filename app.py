from flask import Flask, render_template, request
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from tables import User, Base


TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format("root", "12345678", "flask_app"),
                               pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/')
def index():
    return render_template('login.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        user =  session.query(User).filter(
            User.username == username,
            User.password == password
        ).first()
        if (user):
            return render_template('index.html')
        else:
            return "Error el usuario {} no\
                se encuentra registrado".format(username)

if __name__ == '__main__':
    app.run(debug=True)