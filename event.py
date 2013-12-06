from datetime import datetime

class Event():
    def __init__(self, y, m, d, hour, minute, title):
        self.date = datetime(y, m, d, hour=hour, minute=minute)
        self.title = title
        self.datestr = str(self.date)
        mstr = ""
        if m == 1:
            mstr = "Jan"
        elif m == 2:
            mstr = "Feb"
        elif m == 3:
            mstr = "Mar"
        elif m == 4:
            mstr = "Apr"
        elif m == 5:
            mstr = "May"
        elif m == 6:
            mstr = "Jun"
        elif m == 7:
            mstr = "Jul"
        elif m == 8:
            mstr = "Aug"
        elif m == 9:
            mstr = "Sep"
        elif m == 10:
            mstr = "Oct"
        elif m == 11:
            mstr = "Nov"
        elif m == 12:
            mstr = "Dec"
        today = str(datetime.today())
        evdate = str(self.date)
        if today[0:10] == evdate[0:10]:
            self.datestr = "Today" 
        else:
            self.datestr = mstr + " " + str(d)
        
    def __str__(self):
        return "%s - %s, real date: %s"%(e.datestr, e.title, e.date)

    def should_show(self):
        today = datetime.today()
        return today.date() <= self.date.date() and (today.date() < self.date.date() or (today.hour <= self.date.hour and int(self.date.hour) != 0 and int(self.date.minute) != 0))
        ret = self.date.year >= today.year
        
        return (self.date.hour >= today.hour and
                
                self.date.month >= today.month and
                self.date.day >= today.day)

#events = [Event(1000, 1, 27, 5, 00, "hello")]

def form(e):
    return "%s - %s, real date: %s"%(e.datestr, e.title, e.date)

def organize(events):
    today = datetime.today()
    events = sorted([e for e in events if e.should_show()], key=lambda e: e.date)
    return events

e = Event(2013, 1, 23, 1, 2, "Today do this")
print form(e)

e1 = Event(2013, 12, 6, 1, 2, "lalalalal")
print form(e1)
