from flask import Flask
from flask import request, render_template, redirect, session
from pymongo import MongoClient

import utils
import mta2
import weather
import event

#---------------COMMENTS ARE EITHER EXPLANATIONS OR OLD CODE---------------

c = MongoClient()
db = c['test']
events = db.events

app = Flask(__name__)
app.secret_key = 'jasoniscool'

@app.route("/test")
def test():
	temp = weather.getTemp()
	sky = weather.getWeather()
	return render_template("test.html", temperature = temp, weather = sky, ott = mta2.ott(), ffs = mta2.ffs(), seven = mta2.seven(), ace = mta2.ace(), bdfm = mta2.bdfm(), g = mta2.g(), jz = mta2.jz(), l = mta2.l(), nqr = mta2.nqr(), s = mta2.s(), sir = mta2.sir())

@app.route("/home")
def h():
        return render_template("home.html")

@app.route("/index")
def index():
	return render_template("index.html")

@app.route('/calendar', methods = ['GET', 'POST'])
def cal():
    if request.method =='GET':
        now = datetime.datetime.now()
        yr = now.year
        mo = now.month -1
        el = makeAndDisplayEvents(yr,mo)
        return render_template('calendar.html', event_list=json.dumps([[e.title for e in d] for d in el]))
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
        e = Event(y,m+1,d,h,mi,de)

        addEvent(e)

        el = makeAndDisplayEvents(y,m)

        return render_template('calendar.html', event_list=json.dumps([[e.title for e in d] for d in el]))

@app.route('/calendar/<int:year>/<int:month>', methods = ['GET', 'POST'])
def getCal(year, month):

    if request.method =='GET':
        el = makeAndDisplayEvents(year,month)
        return render_template('calpage.html', y=year, m=month, event_list=json.dumps([[e.title for e in d] for d in el]))
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

        addEvent(e)

        el = makeAndDisplayEvents(year,month)

        return render_template('calpage.html', y=year, m=month, event_list=json.dumps([[e.title for e in d] for d in el]))

def makeAndDisplayEvents(year,month):
    nmonth = month +1
    monstr = str(nmonth)
    yrstr = str(year)
    monthlyEvents = []
    numdays = 31

    if month == 0: 
        numdays = 31
    elif (month == 1): 
        if y % 4 == 0:
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
        monthlyEvents.append(getEvent(yrstr, monstr,i))
        i += 1

    return monthlyEvents

@app.route("/")
def home():
	#trains = [mta2.ott(), mta2.ffs(), mta2.seven(), mta2.ace(), mta2.bdfm(), mta2.g(), mta2.jz(), mta2.l(), mta2.nqr(), mta2.s(), mta2.sir()]
	temp = weather.getTemp()
	sky = weather.getWeather()
	#service = []
	#for x in trains:
	#	service.append(x[1])
	#service = [x[1] for x in trains]
        if "username" in session: #if logged in already
		username = session["username"]
                return render_template("about.html", temperature = temp, weather = sky, ott = mta2.ott(), ffs = mta2.ffs(), seven = mta2.seven(), ace = mta2.ace(), bdfm = mta2.bdfm(), g = mta2.g(), jz = mta2.jz(), l = mta2.l(), nqr = mta2.nqr(), s = mta2.s(), sir = mta2.sir())
                				      #greeting = utils.getName(username)
                				       #should have variables in html that correspond to these
         #if not logged in
	else:
		return redirect("/login")


@app.route("/login",methods=['GET','POST'])
def login():
        if request.method=="GET":
                return render_template("login.html")
        username = request.form['name']
        password = request.form['password']
	if not username or not password:    #there are empty fields
		return render_template("login.html", message = "Please fill out the empty fields!")
	elif utils.auth(username, password, db): #login successful
		session["username"] = username
		return redirect("/")
 	# unsuccessful login
	else:
		return render_template("login.html", message = "Incorrect username and password combination.")

@app.route("/register",methods = ["GET","POST"])
def register():
        if request.method=="GET":
                return render_template("register.html")
	username = request.form['name']
        password = request.form['password']
        confirmPW = request.form['confirm']
        box = request.form.get("acceptTerms")
        if password != confirmPW: #if the two pw's don't match
                return render_template("register.html", message = "Your passwords do not match.")
        elif not box: #if terms and conditions box is not checked
                return render_template("register.html", message = "Please check the terms and conditions.")
        elif not username or not password or not confirmPW: #if not all fields are filled
                return render_template("register.html", message = "Please fill in all of the fields.")
        elif utils.checkUser(username): #if username is taken
                return render_template("register.html", message = "Username already taken. Please find another.")
        else :
                utils.addUser(username, password, db)
                return redirect("/") #send user back home


@app.route("/settings", methods = ["GET", "POST"])
def settings():
	if "username" not in session: #not logged in
		return redirect("/login")
        if request.method=="GET":
                return render_template("settings.html")
        name = request.form['name'] #who you want to be greeted as
        location = request.form['location'] #where you are
        button = request.form['submit'] #this will be whichever button you've pressed: to change name or location
        #oldPW = request.form['oldPW']
        #newPW = request.form['newPW'] ------change password maybe? will leave this here.-----
        #confirmNPW = request.form['cNPW']
        #if "username" not in session: 
          #      return redirect("/login")
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
	app.run(host="0.0.0.0", port=5050)
