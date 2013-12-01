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
    
def addEvent(user, event, coll): #adds events
    coll.insert({'username': user},{'event': event}) #possibly return values if there is a sucess or not?

def changeName(user, name): #changes name
    coll.update({'username': user},{'$set':{'name': 'name'}})
    
def checkUser(username, coll): #this is auth without the password
    return [ x for x in coll.find ({'username': user})] != []
