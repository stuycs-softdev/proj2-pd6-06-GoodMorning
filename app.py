from flask import Flask
from pymongo import MongoClient

import utils

db = MongoClient().db

app = Flask(__name__)
app.secret_key = 'jasoniscool'


@app.route("/")


@app.route("/login",methods=['GET','POST'])

        
@app.route("/register",methods = ["GET","POST"])




@app.route("/settings", methods = ["GET", "POST"])

@app.route("/logout")

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
