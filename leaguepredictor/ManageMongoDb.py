import urllib3
import pycurl
import io
import json
from collections import namedtuple
from enum import Enum
import time
from pymongo import *
import pymongo
from apicalls import *
class DbInstance(object):
    def __init__(self,address,apikey,dbName,unique = 'id',tablename=None):
        if(tablename == None):
            self.tablename = dbName
        else:
            self.tablename = tablename
        self.database = MongoClient(address)#"localhost:27017"
        self.apikey = apikey #'b2d83f48-63fc-44f8-9a03-07d0aa8d16e9'#'7fc833b6-14de-4e95-96a1-a3963876616d'
        self.dbname = dbName
        db = self.database[self.dbname]
        result = db.profiles.create_index([(unique, pymongo.ASCENDING)],unique=True)
        self.unique = unique
    def insertChampions(self):
        apikey = self.apikey
        myregion = regions.na
        myversion = versions.oneFour
        variables = {}
        call = apicalls.staticChampionList
        result = callApi(call,apikey,variables,myversion,myregion)
        client = self.database
        db = client[self.dbname]
        db.posts.remove()
        db = client[self.dbname]
        posts = db.posts
        collection = db[self.dbname]
        print(result)
        print(json.dumps(result['data'].items()))
        dictlist = []
        for key, value in result['data'].items():
            temp = [key,value]
            dictlist.append(value)
        print dictlist
        #posts.insert(dictlist)
        self.insertElements(dictlist)
        post_id = posts.find()
        db.profiles.create_index([('id', pymongo.ASCENDING)],unique=True)
        print(post_id)
    def getAllElements(self,tablename = None):
        if(tablename == None):
            tablename = self.tablename
        client = self.database
        db = client[tablename]
        return list(db.posts.find())
    def getElement(self,id,key="id",tablename = None):
        if(tablename == None):
            tablename = self.tablename
        client = self.database
        db = client[tablename]
        return list(db.posts.find({key:id}))
    def getInsertDate(self,id, key="id",tablename = None):
        if(tablename==None):
            tablename = self.tablename
        db = self.database[self.dbname]
        posts = db.posts
        result = posts.find_one({"id":id})
        return result['inserted']
    def insertElement(self,element,tablename=None):
        if(tablename == None):
            tablename = self.tablename
        element['inserted']=time.time()
        db = self.database[tablename]
        posts = db.posts
        posts.insert_one(element)
    def insertElements(self,elements,tablename = None):
        if(tablename == None):
            tablename = self.tablename
        temeNow = time.time()
        for element in elements:
            element['inserted']=time.time()
        db = self.database[tablename]
        posts = db.posts
        posts.insert(elements)
    def insertOrReplaceElement(self,element,tablename = None):
        if(tablename == None):
            tablename = self.tablename
        if(tablename == None):
            tablename = self.tablename
        element['inserted']=time.time()
        db = self.database[tablename]
        posts = db.posts
        posts.update({self.unique: element[self.unique]}, element, upsert = True)
        '''
inserter = DbInstance("localhost:27017",'7fc833b6-14de-4e95-96a1-a3963876616d',"league_champs")
inserter.insertChampions()
print(inserter.getAllElements())
print(inserter.getElement(67))
tempvalue = inserter.getElement(67)[0]
tempvalue['name']='vaynetest'
inserter.insertOrReplaceElement(tempvalue)
print(inserter.getAllElements())
tempvalue = inserter.getElement(67)[0]
tempvalue['name']='vayne'
tempvalue['inserted']=time.time()
inserter.insertOrReplaceElement(tempvalue)
print(inserter.getElement(67))
'''
#cmd: sudo mongod
#test_database