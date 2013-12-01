from flask import Flask, request, render_template
from event import Event
from datetime import datetime
import utils
import json

app = Flask(__name__)

@app.route('/calendar', methods = ['GET', 'POST'])
def cal():
    e1 = Event(2013,12,1,2,0,"2:00 - event on Dec 1")
    e2 = Event(2013,12,1,4,0,"4:00 - event on Dec 1")
    e3 = Event(2013,12,2,2,0,"2:00 - event on Dec 2")
    e4 = Event(2013,12,6,2,0,"2:00 - event on Dec 6")
    e5 = Event(2013,12,17,2,0,"2:00 - event on Dec 17")
    e6 = Event(2013,12,20,2,0,"2:00 - event on Dec 20")
    e7 = Event(2013,12,20,3,0,"3:00 - event on Dec 20")
    e8 = Event(2013,12,20,4,0,"4:00 - event on Dec 20")
    e9 = Event(2013,12,20,5,0,"5:00 - event on Dec 20")
    e0 = Event(2013,12,25,0,0,"Merry Christmas!")
    
    December2013 = [ [e1,e2], [e3], [], [], [], [e4], [], [], [], [], [], [], [], [], [], [], [e5], [], [], [e6,e7,e8,e9], [], [], [], [], [e0], [], [], [], [], [], [] ]

    if request.method =='GET':
        return render_template('calendar.html', event_list=json.dumps([[e.title for e in d] for d in December2013]))
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

        #print(e.date)
        #print(e.title)
        

        return render_template('calpage.html', event_list=json.dumps([[e.title for e in d] for d in December2013]))

@app.route('/calendar/<int:year>/<int:month>', methods = ['GET', 'POST'])
def getCal(year, month):

    e1 = Event(2013,12,1,2,0,"2:00 - event on Dec 1")
    e2 = Event(2013,12,1,4,0,"4:00 - event on Dec 1")
    e3 = Event(2013,12,2,2,0,"2:00 - event on Dec 2")
    e4 = Event(2013,12,6,2,0,"2:00 - event on Dec 6")
    e5 = Event(2013,12,17,2,0,"2:00 - event on Dec 17")
    e6 = Event(2013,12,20,2,0,"2:00 - event on Dec 20")
    e7 = Event(2013,12,20,3,0,"3:00 - event on Dec 20")
    e8 = Event(2013,12,20,4,0,"4:00 - event on Dec 20")
    e9 = Event(2013,12,20,5,0,"5:00 - event on Dec 20")
    e0 = Event(2013,12,25,0,0,"Merry Christmas!")
    
    December2013 = [ [e1,e2], [e3], [], [], [], [e4], [], [], [], [], [], [], [], [], [], [], [e5], [], [], [e6,e7,e8,e9], [], [], [], [], [e0], [], [], [], [], [], [] ]


    if month < 0:
        year -= 1
        month = 12 - month
    elif month > 11:
        year += 1
        month = month - 12
    if request.method =='GET':
        return render_template('calendar.html', y=year, m=month, event_list=json.dumps([[e.title for e in d] for d in December2013]))
    else:
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
        e = Event(year,month,d,h,mi,de)

        return render_template('calendar.html', y=year, m=month, event_list=json.dumps([[e.title for e in d] for d in December2013]))

app.debug=True
app.run(host='0.0.0.0',port=5000)

