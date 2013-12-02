from flask import Flask, redirect, request, render_template
from event import Event
import datetime
import utils
import json

app = Flask(__name__)

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
        daystr = str(i)
        monthlyEvents.append(getEvent(yrstr, monstr,daystr))
        i += 1

    return monthlyEvents

app.debug=True
app.run(host='0.0.0.0',port=5000)

