import urllib3
import pycurl
import io
import json
from collections import namedtuple
from enum import Enum
import time
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
class versions(Enum):
    oneTwo = 'v1.2'
    oneFour = 'v1.4'
    twoFour = 'v2.4'
    twoFive = 'v2.5'
class apicalls(Enum):
    summonerByName = '/api/lol/{region}/{version}/summoner/by-name/{summoner}'
    #summonerById = '/api/lol/{region}/{version}/champion/{id}'
    currentGame = '/observer-mode/rest/consumer/getSpectatorGameInfo/{platformId}/{summonerId}'
    featuerdGames = '/observer-mode/rest/featured'
    recentGamesSummoner = '/api/lol/{region}/v1.3/game/by-summoner/{summonerId}/recent'

    leaguesPerSummonerIds = '/api/lol/{region}/v2.5/league/by-summoner/{summonerIds}'
    leaguesPerSummonerIdsEntries = '/api/lol/{region}/v2.5/league/by-summoner/{summonerIds}/entry'
    leaguePerTeamId = '/api/lol/{region}/v2.5/league/by-team/{teamIds}'
    leaguePerTeamIDEntries = '/api/lol/{region}/v2.5/league/by-team/{teamIds}/entry'
    leaguesChallenger = '/api/lol/{region}/v2.5/league/challenger'
    leaguesMaster = '/api/lol/{region}/v2.5/league/master'

    staticChampionList = '/api/lol/static-data/{region}/v1.2/champion'
    staticChampionId = '/api/lol/static-data/{region}/v1.2/champion/{id}'
    staticItemList = '/api/lol/static-data/{region}/v1.2/item'
    staticLanguageList = '/api/lol/static-data/{region}/v1.2/language-strings'
    staticSupportedLanguagesData = '/api/lol/static-data/{region}/v1.2/languages'
    staticMapData = '/api/lol/static-data/{region}/v1.2/map'
    staticMasteryList = '/api/lol/static-data/{region}/v1.2/mastery'
    staticMateryId = '/api/lol/static-data/{region}/v1.2/mastery/{id}'
    staticRealmData = '/api/lol/static-data/{region}/v1.2/realm'
    staticRuneList = '/api/lol/static-data/{region}/v1.2/rune'
    staticRuneId = '/api/lol/static-data/{region}/v1.2/rune/{id}'
    staticSpellList = '/api/lol/static-data/{region}/v1.2/summoner-spell'
    staticSpellId = '/api/lol/static-data/{region}/v1.2/summoner-spell/{id}'
    staticVersionData = '/api/lol/static-data/{region}/v1.2/versions'

    statusSharedList = '/shards'
    statusSharedRegion = '/shards/{region}'

    matchIdByTournamentCodeIds = '/api/lol/{region}/v2.2/match/by-tournament/{tournamentCode}/ids'
    matchByMatchAndTournamentCode = '/api/lol/{region}/v2.2/match/for-tournament/{matchId}'
    matchByMatchId = '/api/lol/{region}/v2.2/match/{matchId}'
    matchListBySummoner = '/api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}'

    statsRankedBySummonerId = '/api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/ranked'
    statsSummariesBySummonerId = '/api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/summary'

    SummonerBySummonerNames = '/api/lol/{region}/v1.4/summoner/by-name/{summonerNames}'
    SummonerBySummonerIds = '/api/lol/{region}/v1.4/summoner/{summonerIds}'
    SummonerMasteryPagesBySummonerIds = '/api/lol/{region}/v1.4/summoner/{summonerIds}/masteries'
    SummonerNamesByIds = '/api/lol/{region}/v1.4/summoner/{summonerIds}/name'
    summonerRunePagesBySummonerIds = '/api/lol/{region}/v1.4/summoner/{summonerIds}/runes'

    teamsBySummonerids = '/api/lol/{region}/v2.4/team/by-summoner/{summonerIds}'
    teamsByTeamId = '/api/lol/{region}/v2.4/team/{teamIds}'
class apiCaller:
    keys = ['7fc833b6-14de-4e95-96a1-a3963876616d','b2d83f48-63fc-44f8-9a03-07d0aa8d16e9']#'7fc833b6-14de-4e95-96a1-a3963876616d']

    def __init__(self):
        self.keytimes = [0]*len(self.keys)
        self.minDifference = [2.0]*len(self.keys)
        self.pos=0
    def callApi(self,call, apikey, variables = {},myversion=versions.twoFive,myregion=regions.euw):
        buffer = io.BytesIO()
        c = pycurl.Curl()
        url = call.value
        print(url)
        url = url.replace('{version}',myversion.value)
        url = url.replace('{region}',myregion.value)
        for key,value in variables.items():
            url = url.replace('{'+key+'}',str(value))
        print('url is '+url)
        constructedUrl = 'https://'+str(myregion.value)+'.api.pvp.net'+url+'?api_key='+apikey
        print(constructedUrl)
        diff = self.minDifference[self.pos]-(time.time()- self.keytimes[self.pos])
        if diff>0:
            time.sleep(diff)
        time.sleep(2)
        c.setopt(c.URL, constructedUrl)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        print("result is")
        print((buffer.getvalue().decode("utf-8")))
        result = json.loads((buffer.getvalue().decode("utf-8")))
        self.keytimes[self.pos] = time.time()
        self.pos = (self.pos+1)%2
        return result
