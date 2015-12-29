import urllib3
import pycurl
import io
import json
from collections import namedtuple
from enum import Enum
from pymongo import *
import pymongo
from apicalls import *
class champions(object):
    def __init__(self,address,apikey):
        self.database = MongoClient(address)#"localhost:27017"
        self.apikey = apikey #'b2d83f48-63fc-44f8-9a03-07d0aa8d16e9'#'7fc833b6-14de-4e95-96a1-a3963876616d'
    def insertChampions(self):
        apikey = self.apikey
        myregion = regions.na
        myversion = versions.oneFour
        variables = {}
        call = apicalls.staticChampionList
        result = callApi(call,apikey,variables,myversion,myregion)
        client = self.database
        db = client.test_database
        db.posts.remove()
        db = client.test_database
        posts = db.posts
        collection = db.league_champs
        print(json.dumps(result['data'].items()))
        dictlist = []
        for key, value in result['data'].items():
            temp = [key,value]
            dictlist.append(value)
        print dictlist
        posts.insert(dictlist)
        post_id = posts.find()
        db.profiles.create_index([('id', pymongo.ASCENDING)],unique=True)
        print(post_id)
    def getChampions(self):
        client = self.database
        db = client.test_database
        return list(db.posts.find())
    def getChampion(self,id):
        client = self.database
        db = client.test_database
        return list(db.posts.find({'id':id}))
inserter = champions("localhost:27017",'7fc833b6-14de-4e95-96a1-a3963876616d')
inserter.insertChampions()
print(inserter.getChampions())
print(inserter.getChampion(67))
#cmd: sudo mongod