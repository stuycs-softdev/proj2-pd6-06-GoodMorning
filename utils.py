from pymongo import MongoClient


def auth(user, password, coll):
    return [ x for x in coll.find ({'username': user, 'password':password})] != []

def addUser(user, password, coll): #adds user
    coll.insert({'username': user, 'password':password})

def addLocation(user, location): #adds location
    coll.insert({'username': user, 'location': location})

def getLocation(location, coll): #returns location
    return [x for x in coll.find ({'location':location})]

def changeLocation(location): #changes location
    coll.update({'$set':{'location': 'location'}}) 
    
def addEvent(event): #adds events
    coll.insert({'event': event}) #possibly return values if there is a sucess or not?

def changeName(name): #changes name
    coll.update({'$set':{'name': 'name'}})
    
def checkUser(username, coll): #this is auth without the password
    return [ x for x in coll.find ({'username': user})] != []
