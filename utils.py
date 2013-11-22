from pymongo import MongoClient


def auth(user, password, coll):
    return [ x for x in coll.find ({'username': user, 'password':password})] != []

def addUser(user, password, coll):
    coll.insert({'username': user, 'password':password}]

def addLocation(user, location):
    coll.insert({'username': user, 'location': location})

def getLocation(location, coll):
    return [x for x in coll.find ({'location':location})

def changeLocation(username, location):
    
def addEvent():

def changeName(username, name):
    
def checkUser(username):
    
