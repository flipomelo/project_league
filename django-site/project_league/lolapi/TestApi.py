import urllib3
import pycurl
import io
import json
from collections import namedtuple
from enum import Enum
from apicalls import *
summoner = 'RiotSchmick'
apikey = 'b2d83f48-63fc-44f8-9a03-07d0aa8d16e9'#'7fc833b6-14de-4e95-96a1-a39638$
myregion = regions.na
myversion = versions.oneFour
variables = {'summoner':'RiotSchmick'}
call = apicalls.summonerByName
result = callApi(call,apikey,variables,myversion,myregion)
print(result['riotschmick']['id'])
variables['summonerId'] = result['riotschmick']['id']
call = apicalls.matchListBySummoner
result = callApi(call,apikey,variables,myversion,myregion)
print(result)
