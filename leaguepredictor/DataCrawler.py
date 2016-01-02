from CallManager import *
from apicalls import *
from ManageMongoDb import *
import pymongo
caller = apiCaller()
minscore = 1
summonersDb = DbInstance("localhost:27017",'7fc833b6-14de-4e95-96a1-a3963876616d',"league_summoners",tablename="summonersSummary")
matchesDb = DbInstance("localhost:27017",'7fc833b6-14de-4e95-96a1-a3963876616d',"league_matches")
#summoner = 'heremoddd'
apikey = '7fc833b6-14de-4e95-96a1-a3963876616d'#'b2d83f48-63fc-44f8-9a03-07d0aa8d16e9'#'7fc833b6-14de-4e95-96a1-a3963876616d'
myregion = regions.euw
myversion = versions.oneFour
score = 1024
mindate = time.time()-24*3600*10
insertDate = mindate
variables = {'summoner':'flipwithagun'}
call = apicalls.summonerByName
result = caller.callApi(call,apikey,variables,myversion,myregion)
print(result)
startElement = CrawlerElement("summoner",result.values()[0]['id'],score,mindate)
queue = CrawlerQueue([startElement])
while(queue.count()>0):
    elementNow = queue.pop()
    #if elementNow._elem == "summoner":
    variables = {'summonerIds':elementNow._id,'summonerId':elementNow._id}
    newScore = elementNow._score/2
    call = apicalls.SummonerBySummonerIds
    result = caller.callApi(call,apikey,variables,versions.oneFour,myregion = regions.euw)
    #newScore = score/2
    for res in result.values():
        print(result)
        print(res)
        summonersDb.insertOrReplaceElement(res)
        call = apicalls.recentGamesSummoner
        matchResult = caller.callApi(call,apikey,variables,versions.oneFour,myregion = regions.euw)
        print(matchResult)
        for match in matchResult['games']:
            print("match is "+str(match))
            match['id']=match['gameId']
            del match['gameId']
            matchesDb.insertOrReplaceElement(match,tablename=match['gameMode'])
            if newScore>=minscore:
                for match in match['fellowPlayers']:
                    newElement = CrawlerElement("summoner",match['summonerId'],newScore,mindate)
                    queue.add(newElement)
        print matchResult
    #raise error("stop here")
    #else:
    #    variables = {'summonerId':elementNow._id}
    #    call = apicalls.matchListBySummoner
    #    result = callApi(call,apikey,variables,versions.oneFour,myregion = 'euw')
    #    for res in result:
    #        print(res)
    #        raise error("stop here")
    #        matchesDb.insertOrReplaceElement(result)

'''
variables = {'summoner':'heremoddd'}
call = apicalls.summonerByName
result = callApi(call,apikey,variables,myversion,myregion)
#variables['summonerId'] = result['riotschmick']['id']
#call = apicalls.matchListBySummoner
#result = callApi(call,apikey,variables,myversion,myregion)
print((result.values()[0])['id'])
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20)
queue = CrawlerQueue()
queue.add(queueEl)
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20)
queue.add(queueEl)
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20)
queue.add(queueEl)
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20)
queue.add(queueEl)
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20)
queue.add(queueEl)
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20)
queue.add(queueEl)
el = queue.pop()
print(el._score)
print(el._id)
print(el._elem)
'''