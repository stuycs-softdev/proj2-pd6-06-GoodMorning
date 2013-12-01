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

def organize(events):
    today = datetime.today()
    print 'today is', events[0].date.year >= today.hour
    events = sorted([e for e in events if e.should_show()], key=lambda e: e.date)
    return events
        
