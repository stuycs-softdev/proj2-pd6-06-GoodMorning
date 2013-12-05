from flask import Flask
from flask import request, render_template, redirect, session
from pymongo import MongoClient
from datetime import datetime
from event import Event
import utils
import mta2
import weather
import json

#---------------COMMENTS ARE EITHER EXPLANATIONS OR OLD CODE---------------

#c = MongoClient()
#db = c['test']
#events = db.events

app = Flask(__name__)
app.secret_key = 'jasoniscool'

@app.route("/")
def about():
	if "username" not in session:
		return render_template("about.html")
        else:
		return redirect("/homepage")

@app.route('/calendar', methods = ['GET', 'POST'])
def cal():
    if request.method =='GET':
        now = datetime.now()
        yr = now.year
        mo = now.month -1
        el = makeAndDisplayEvents(yr,mo)
        return render_template('calendar.html', event_list=json.dumps([[ev.title for ev in d] for d in el]))
    else:
        #print (request.form['year'] + " " + request.form['month'] + " " + request.form['day'] + " " + request.form['starthour'] + ":" + request.form['startmin'] + request.form['amorpm1'] + "-" + request.form['endhour'] + ":" + request.form['endmin'] + request.form['amorpm2'] + " - " + request.form['newevent'])
        inclTime = True
        y = (int)(request.form['year'])
        mon = request.form['month']
        if mon == "January":
            m = 1
        elif mon == "February":
            m = 2
        elif mon == "March":
            m = 3
        elif mon == "April":
            m = 4
        elif mon == "May":
            m = 5
        elif mon == "June":
            m = 6
        elif mon == "July":
            m = 7
        elif mon == "August":
            m = 8
        elif mon == "September":
            m = 9
        elif mon == "October":
            m = 10
        elif mon == "November":
            m = 11
        elif mon == "December":
            m = 12
        d = (int)(request.form['day'])
        if request.form['starthour'] == "":
            h = 0
            inclTime = False
        else:
            if request.form['amorpm1'] == "PM":
                h = (int)(request.form['starthour']) + 12
            else:
                h = (int)(request.form['starthour'])
        if request.form['startmin'] == "":
            mi = 0
            inclTime = False
        else:
            mi = (int)(request.form['startmin'])
        if inclTime:
            de = request.form['starthour'] + ":" + request.form['startmin'] + request.form['amorpm1'] + "-" + request.form['endhour'] + ":" + request.form['endmin'] + request.form['amorpm2'] + " - " + request.form['newevent']
        else:
            de = request.form['newevent']
	e = Event(y,m,d,h,mi,de)

        utils.addEventObject(session["username"], e)

        el = makeAndDisplayEvents(y,m-1)

        return render_template('calendar.html', event_list=json.dumps([[ev.title for ev in d] for d in el]))

@app.route('/calendar/<int:year>/<int:month>', methods = ['GET', 'POST'])
def getCal(year, month):

    if request.method =='GET':
        el = makeAndDisplayEvents(year,month)
        return render_template('calpage.html', y=year, m=month, event_list=json.dumps([[ev.title for ev in d] for d in el]))
    else:
        d = (int)(request.form['day'])
        inclTime = True
        inclEndTime = True
        if request.form['starthour'] == "":
            h = 0
            inclTime = False
        else:
            if request.form['amorpm1'] == "PM":
                h = (int)(request.form['starthour']) + 12
            else:
                h = (int)(request.form['starthour'])
        if request.form['startmin'] == "":
            mi = 0
            inclTime = False
        else:
            mi = (int)(request.form['startmin'])
        if ((request.form['endhour'] == "") or (request.form['endhour'] == "")):
            inclEndTime = False
        if inclTime and inclEndTime:
            de = request.form['starthour'] + ":" + request.form['startmin'] + request.form['amorpm1'] + "-" + request.form['endhour'] + ":" + request.form['endmin'] + request.form['amorpm2'] + " - " + request.form['newevent']
        elif inclTime:
            de = request.form['starthour'] + ":" + request.form['startmin'] + request.form['amorpm1'] + " - " + request.form['newevent']
        else:
            de = request.form['newevent']
        e = Event(year,month+1,d,h,mi,de)

        utils.addEventObject(session["username"],e)

        el = makeAndDisplayEvents(year,month)

        return render_template('calpage.html', y=year, m=month, event_list=json.dumps([[ev.title for ev in d] for d in el]))

def makeAndDisplayEvents(year,month):
    nmonth = month
    monstr = str(nmonth)
    yrstr = str(year)
    monthlyEvents = []
    numdays = 31

    if month == 0: 
        numdays = 31
    elif (month == 1): 
        if year % 4 == 0:
            numdays = 29
        else: 
            numdays = 28
    elif (month == 2):
        numdays = 31
    elif (month == 3): 
        numdays = 30
    elif (month == 4): 
        numdays = 31
    elif (month == 5):              
        numdays = 30
    elif (month == 6): 
        numdays = 31
    elif (month == 7): 
        numdays = 31
    elif (month == 8): 
        numdays = 30
    elif (month == 9):
        numdays = 31
    elif (month == 10): 
        numdays = 30
    elif (month == 11): 
        numdays= 31

    i = 1
    while (i <= numdays): 
        daystr = str(i)
        evlist = utils.getEvent(session["username"],yrstr, monstr,daystr)
        monthlyEvents.append(evlist)
        i += 1

    return monthlyEvents

@app.route("/homepage")
def home():
        #trains = [mta2.ott(), mta2.ffs(), mta2.seven(), mta2.ace(), mta2.bdfm(), mta2.g(), mta2.jz(), mta2.l(), mta2.nqr(), mta2.s(), mta2.sir()]
        temp = weather.getTemp()
        sky = weather.getWeather()
        if "username" in session: #if logged in already
                username = session["username"]
                return render_template("homepage.html", username = username, temperature = temp, weather = sky, ott = mta2.ott(), ffs = mta2.ffs(), seven = mta2.seven(), ace = mta2.ace(), bdfm = mta2.bdfm(), g = mta2.g(), jz = mta2.jz(), l = mta2.l(), nqr = mta2.nqr(), s = mta2.s(), sir = mta2.sir())
                                                      #greeting = utils.getName(username)                                                       
         #if not logged in
        else:
                return redirect("/")


@app.route("/login",methods=["GET","POST"])
def login():
        if request.method=="GET":
                return render_template("login.html")
        username = request.form['name']
        password = request.form['password']
	print username
	print password
        if not username or not password:    #there are empty fields
		print "1"
                return render_template("login.html", message = "Please fill out the empty fields!")
        elif utils.login(username, password): #login successful
		print "2"
                session["username"] = username
                return redirect("/homepage")
         # unsuccessful login
        else:
		print "3"
                return render_template("login.html", message = "Incorrect username and password combination.")

@app.route("/register",methods = ["GET","POST"])
def register():
        if request.method=="GET":
                return render_template("register.html")
        username = request.form['name']
        password = request.form['password']
        confirmPW = request.form['confirm']
        nickname = request.form['nickname']
	#print username 
	#print password
	#print confirmPW
	#print nickname
        if not username or not password or not confirmPW: #not all of the fields are filled
		#print "Please fill in all of the fields."
                return render_template("register.html", message = "Please fill in all of the fields.")
        elif password != confirmPW: #if the two pw's don't match
		#print  "Your passwords do not match."
                return render_template("register.html", message = "Your passwords do not match.")
        elif utils.register(username, password, nickname): #if username is taken
		session["username"] = username
		print "success!"
                return redirect("/") #send user back home
        else:
		#print "Username already taken. Please find another."
                return render_template("register.html", message = "Username already taken.")



@app.route("/logout")
def logout():
        session.pop("username", None)
        return redirect("/") #or maybe redirect to login? idk.


if __name__=="__main__":
        app.debug=True
        app.run(port=5000)
