import urllib3
import pycurl
import io
import json
from collections import namedtuple
from enum import Enum
from pymongo import *
from apicalls import *
import datetime
summoner = 'RiotSchmick'
apikey = 'b2d83f48-63fc-44f8-9a03-07d0aa8d16e9'#'7fc833b6-14de-4e95-96a1-a3963876616d'
myregion = regions.na
myversion = versions.oneFour
variables = {'summoner':'RiotSchmick'}
call = apicalls.summonerByName
result = callApi(call,apikey,variables,myversion,myregion)
variables['summonerId'] = result['riotschmick']['id']
call = apicalls.matchListBySummoner
result = callApi(call,apikey,variables,myversion,myregion)
call = apicalls.staticChampionList
result = callApi(call,apikey,variables,myversion,myregion)
client = MongoClient()
client = MongoClient("localhost:27017")
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
post_id = posts.find().count()
posts.remove()
print(post_id)
