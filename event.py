from datetime import datetime

class Event():
    def __init__(self, y, m, d, hour, minute, title):
        self.date = datetime(y, m, d, hour=hour, minute=minute)
        self.title = title
    
    def __str__(self):
        return '%s at %s'%(self.title, self.date)

    def should_show(self):
        today = datetime.today()
        return today.date() <= self.date.date() and (today.date() < self.date.date() or today.hour <= self.date.hour)
        ret = self.date.year >= today.year
        
        return (self.date.hour >= today.hour and
              
                self.date.month >= today.month and
                self.date.day >= today.day)

#events = [Event(1000, 1, 27, 5, 00, "hello")]

def organize(events):
    today = datetime.today()
    print 'today is', events[0].date.year >= today.hour
    events = sorted([e for e in events if e.should_show()], key=lambda e: e.date)
    return events


import random
def test(i=15):
    popsicle = []
    while i > 0:
        year = random.choice(range(2013, 2015))
        month = random.choice(range(1, 13))
        day = random.choice(range(1, 28))
        hour = random.choice(range(0, 24))
        minute = random.choice(range(0, 60))
        popsicle.append(Event(year, month, day, hour, minute, 'Event %d'%i))
        i -= 1
#    print 'unsorted:', [form(e) for e in popsicle]
    print 'sorted:', [form(e) for e in organize(popsicle)]

def form(e):
    return "%s at %s"%(e.title, e.date)

test()        