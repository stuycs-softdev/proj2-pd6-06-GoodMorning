from pymongo import MongoClient
from event import Event

def open():
    client = MongoClient()
    db = client.gm.users
    return db
    
#------------ADDING USERS--------------------------------------------------
def register(username, password, nickname):
    db = open()
    check = db.find_one({'username' : username}, fields={'_id':False})
    if check == None:
        db.insert({'username' : username, 'password' : password, 'nickname' : nickname})
        return True
    else:
        return False
        
#----------NOT USING THIS--------------(probably)-------------------------
def checkForName(username):
    db = open()
    user = db.find_one({'username' : username}, fields={'_id':False})
    if not user == None:
        return False
    else:
        return True
        
#-------------LOGIN-----------------------------------------------------
def login(username, password):
    db = open()
    user = db.find_one({'username' : username, 'password' : password}, fields={'_id':False})
    if user == None:
        return False
    else:
        return True
        
#----------------USER MANAGEMENT--------------------------------
def updateSettings(username, nickname, train1, train2, train3, email):
    db = open()
    user = db.find_one({'username' : username}, fields={'_id':False})
    if user == None:
        return False
    else:
        db.update({'username' : username}, {'$set':{'nickname':nickname,'train1':train1, 'train2':train2, 'train3':train3, 'email':email}})
        return True


def changePW(username, newpassword):
    db = open()
    user = db.find_one({'username' : username}, fields={'_id':False})
    if user == None:
        return False
    else:
        db.update({'username' : username}, {'$set':{'password':newpassword}})
        return True
#----------------Events--------------------------------
def addEventObject(username, e):
    d = e.date
    addEvent(username, d.year, d.month, d.day, d.hour, d.minute, e.title)

def addEvent(username, year, month, date, hour, minute, title):
    db=open()
    db.insert({'username': username, 'year': year, 'month': month,
               'date':date, 'hour': hour, 'minute':minute,
               'title': title})

def getEvent(username, year, month, date):
    db = open()
    res = db.find({'username': username, 'year':year, 'month':month, 'date':date})
    return [Event(int(e['year']), int(e['month']), int(e['date']),
                  int(e['hour']), int(e['minute']), e['title']) for e in res]
    





#def addEvent(user, year, month, date, hour, minute, title, coll): #adds events
#    coll.insert({'username': user},{'year': year}, {'month': month}, {'date':date}, {'hour': hour}, {'minute':minute},{'title': title}) 

#def getEvent(year, month, date, coll):
#    return coll.find( {'year':year}, {'month':month}, {'date':date})

#def getMonthList(user, month, year, coll):
#    return coll.find({'user':user}, {'month':month}, {'year':year});
#def changePW() ----------might think about implementing this---------- (done! i think)
#def changeNickname() ------------and this-------------later-------- (also done! ...maybe....)


#def auth(user, password, coll):
#    return [ x for x in coll.find ({'username': user, 'password':password})] != []

#def addUser(user, password, coll): #adds user
#    coll.insert({'username': user, 'password':password})

#def addLocation(user, location, coll): #adds location
#    coll.insert({'username': user, 'location': location})

#def getLocation(location, coll): #returns location
#    return [x for x in coll.find ({'location':location})]

#def changeLocation(user, location, coll): #changes location
#    coll.update({'username': user}, {'$set':{'location': 'location'}}) 
    
#def addEvent(user, year, month, date, hour, minute, title, coll): #adds events
#    coll.insert({'username': user},{'year': year}, {'month': month}, {'date':date}, {'hour': hour}, {'minute':minute},{'title': title}) 

#def getEvent(year, month, date, coll):
#    return coll.find( {'year':year}, {'month':month}, {'date':date})

#def getMonthList(user, month, year, coll):
#    return coll.find({'user':user}, {'month':month}, {'year':year});

#def changeName(user, name): #changes name
#    coll.update({'username': user},{'$set':{'name': 'name'}})
    
#def checkUser(username, coll): #this is auth without the password
#    return [ x for x in coll.find ({'username': username})] != []

#def getName(username, coll): #this should return the nickname of a user
