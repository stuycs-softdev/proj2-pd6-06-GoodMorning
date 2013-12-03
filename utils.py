from pymongo import MongoClient


def auth(user, password, coll):
    return [ x for x in coll.find ({'username': user, 'password':password})] != []

def addUser(user, password, coll): #adds user
    coll.insert({'username': user, 'password':password})

def addLocation(user, location, coll): #adds location
    coll.insert({'username': user, 'location': location})

def getLocation(location, coll): #returns location
    return [x for x in coll.find ({'location':location})]

def changeLocation(user, location, coll): #changes location
    coll.update({'username': user}, {'$set':{'location': 'location'}}) 
    
def addEvent(user, year, month, date, hour, minute, title, coll): #adds events
    coll.insert({'username': user},{'year': year}, {'month': month}, {'date':date}, {'hour': hour}, {'minute':minute},{'title': title}) 

def getEvent(year, month, date, coll):
    return coll.find( {'year':year}, {'month':month}, {'date':date})

def getMonthList(user, month, year, coll):
    return coll.find({'user':user}, {'month':month}, {'year':year});

def changeName(user, name): #changes name
    coll.update({'username': user},{'$set':{'name': 'name'}})
    
def checkUser(username, coll): #this is auth without the password
    return [ x for x in coll.find ({'username': username})] != []

#def getName(username, coll): #this should return the nickname of a user
