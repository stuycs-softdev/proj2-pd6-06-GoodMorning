from flask import Flask, request, render_template, redirect, session
from pymongo import MongoClient

import utils

db = MongoClient().db

app = Flask(__name__)
app.secret_key = 'jasoniscool'


@app.route("/")
def home():
        return render_template(homepage.html)


@app.route("/login",methods=['GET','POST'])
def login():
        if request.method=="GET":
                return render_template(login.html)
        username = request.form['name']
        password = request.form['password']
        if not username or not password:    
                return render_template(login.html, message = "Please fill out the empty fields!")
        if utils.auth(username, password, db):
                return redirect("/")
        else:
                return render_template(login.html, message = "Incorrect username and password combination.")
        
@app.route("/register",methods = ["GET","POST"])
        if request.method=="GET":
                return render_template(register.html)
        username = request.form['name']
        password = request.form['password']
        confirmPW = request.form['confirm']
        box = request.form.get("acceptTerms")
        if password != confirmPW:
                return render_template(register.html, message = "Your passwords do not match.")
        if !box:
                return render_template(register.html, message = "Please check the terms and conditions.")
        if not username or not password or not confirmPW:
                return render_template(register.html, message = "Please fill in all of the fields.")
        if !utils.checkUser(username):
                re



@app.route("/settings", methods = ["GET", "POST"])

@app.route("/logout")

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
