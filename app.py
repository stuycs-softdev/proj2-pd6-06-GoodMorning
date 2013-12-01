from flask import Flask, request, render_template, redirect, session
from pymongo import MongoClient

import utils

db = MongoClient().db

app = Flask(__name__)
app.secret_key = 'jasoniscool'


@app.route("/")
def home():
        if "username" in session: #if logged in already
                return render_template(homepage.html)
        else: #if not logged in
                return redirect("/login")


@app.route("/login",methods=['GET','POST'])
def login():
        if request.method=="GET":
                return render_template("login.html")
        username = request.form['name']
        password = request.form['password']
        if not username or not password:    #there are fields that are empty
                return render_template(login.html, message = "Please fill out the empty fields!")
        elif utils.auth(username, password, db): #login successful
                session["username"] = username
                return redirect("/")
        else: #login unsuccessful
                return render_template(login.html, message = "Incorrect username and password combination.")
        
@app.route("/register",methods = ["GET","POST"])
def register():
        if request.method=="GET":
                return render_template(register.html)
        username = request.form['name']
        password = request.form['password']
        confirmPW = request.form['confirm']
        box = request.form.get("acceptTerms")
        if password != confirmPW: #if the two pw's don't match
                return render_template(register.html, message = "Your passwords do not match.")
        elif not box: #if terms and conditions box is not checked
                return render_template(register.html, message = "Please check the terms and conditions.")
        elif not username or not password or not confirmPW: #if not all fields are filled
                return render_template(register.html, message = "Please fill in all of the fields.")
        elif utils.checkUser(username): #if username taken
                return render_template(register.html, message = "Username already taken. Please find another.")
        else :
                utils.addUser(username, password, db)
                return redirect("/") #sends user back home


@app.route("/settings", methods = ["GET", "POST"])
def settings():
        if request.method=="GET":
                return render_template(settings.html)
        name = request.form['name'] #who you want to be greeted as
        location = request.form['location'] #where you are
        button = request.form['submit'] #this will be whichever button you've pressed: to change name or location
        #oldPW = request.form['oldPW']
        #newPW = request.form['newPW'] ------change password maybe? will leave this here.-----
        #confirmNPW = request.form['cNPW']
        if "username" not in session: #not logged in
                return redirect("/login")
        if button == 'changeName':
                utils.changeName(session["username"], name) #to change name
        if button == 'changeLocation':
                utils.changeLocation(session["username"], name) # to change location
        
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/") #or maybe redirect to login? idk.


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
