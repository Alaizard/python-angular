from flask import render_template
from app import app


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template('signup.html')


@app.route("/login", methods=['GET', "POST"])
def login():
    return render_template('login.html')
