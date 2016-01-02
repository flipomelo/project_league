import urllib3
import pycurl
import io
import json
from collections import namedtuple
from enum import Enum

class regions(Enum):
    na = 'na'
    euw = 'euw'
    eune = 'eune'
    kr='kr'
    las = 'las'
    ace = 'oce'
    pbe = 'pbe'
    ru = 'ru'
    tr = 'tr'
    br = 'br'
class version(Enum):
    two = '1.2'
    four = 'v1.4'
class apicalls(Enum):
    summonerByName = '/api/lol/{region}/{version}/summoner/by-name/{summoner}'




summoner = 'RiotSchmick'
apikey = 'b2d83f48-63fc-44f8-9a03-07d0aa8d16e9'#'7fc833b6-14de-4e95-96a1-a3963876616d'
myregion = regions.na
myversion = version.four
call = apicalls.summonerByName
buffer = io.BytesIO()
c = pycurl.Curl()
print(str(myregion.value))
arguments = {}
arguments["summoner"]=summoner
url = call.value
print(url)
url = url.replace('{version}',myversion.value)
url = url.replace('{region}',myregion.value)
for key,value in arguments.items():
    url = url.replace('{'+key+'}',value)
print('url is '+url)
constructedUrl = 'https://'+str(myregion.value)+'.api.pvp.net'+url+'?api_key='+apikey
print(constructedUrl)
c.setopt(c.URL, constructedUrl)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
summoner = json.loads((buffer.getvalue().decode("utf-8")))
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
print(body)

