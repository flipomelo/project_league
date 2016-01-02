from heapq import *
from apicalls import *
from copy import deepcopy
import time
class CrawlerElement(object):
    """
    A proxy for an element in a priority queue that remembers (and
    compares according to) its score.
    """
    def __init__(self, elem, id, score,lastUpdated):
        self._elem = elem
        self._score = score
        self._id = id
        self._removed = False
        self._lastUpdated = lastUpdated

    def __lt__(self, other):
        return self._score-(self._lastUpdated/300) > other._score-(self._lastUpdated/300)
    def copy(self):
        return CrawlerElement(self._elem,self._id,self._score,self._lastUpdated)

class CrawlerQueue(object):
    """
    A priority queue with O(log n) addition, O(1) membership test and
    amortized O(log n) removal.

    The `key` argument to the constructor specifies a function that
    returns the score for an element in the priority queue. (If not
    supplied, an element is its own score).

    The `add` and `remove` methods add and remove elements from the
    queue, and the `pop` method removes and returns the element with
    the lowest score.

    q = PriorityQueue([3, 1, 4])
    q.pop()
    1
    q.add(2); q.pop()
    2
    q.remove(3); q.pop()
    4
    list(q)
    []
    q = PriorityQueue('vext cwm fjord'.split(), key = lambda s:len(s))
    q.pop()
    'cwm'
    """
    def __init__(self, *args, **kwargs):
        self._key = kwargs.pop('key', lambda x:x)
        self._heap = []
        self._dict = {}
        self.counter = 0
        self.heapifAfterNumberElements = 20
        if args:
            for elem in args[0]:
                self.add(elem)

    def __contains__(self, id):
        return id in self._dict

    def __iter__(self):
        return iter(self._dict)

    def add(self, element):
        if(element._id in self._dict):
            oldEl = self._dict[element._id]
            oldEl._removed = True
            newEl = oldEl.copy()
            newEl._score = oldEl._score+element._score
            newEl._removed = False
            self._dict[oldEl._id]=newEl
            heappush(self._heap, newEl)
            self.counter=self.counter+1
            if(self.counter>=self.heapifAfterNumberElements):
                self._heap = self._dict.values()
                theap = heapify(self._heap)
                counter = 0
                #self._heap = theap

        else:
            self._dict[element._id] = element
            heappush(self._heap, element)


    def remove(self, elem):
        """
        Remove an element from a priority queue.
        If the element is not a member, raise KeyError.
        """
        e = self._dict.pop(elem)
        e._removed = True
    def count(self):
        return len(self._dict)
    def pop(self):
        """
        Remove and return the element with the smallest score from a
        priority queue.
        """
        print ("heap len is "+str(len(self._heap)))
        while True:
            heapify(self._heap)
            print("heap is "+str(self._heap))
            print('end print')
            e = heappop(self._heap)
            print(str(e))
            if not e._removed:
                del self._dict[e._id]
                return e
            else:
                self.counter=self.counter-1


"""""
Tests

summoner = 'heremoddd'
apikey = 'b2d83f48-63fc-44f8-9a03-07d0aa8d16e9'#'7fc833b6-14de-4e95-96a1-a3963876616d'
myregion = regions.euw
myversion = versions.oneFour
variables = {'summoner':'RiotSchmick'}
call = apicalls.summonerByName
result = callApi(call,apikey,variables,myversion,myregion)
#variables['summonerId'] = result['riotschmick']['id']
#call = apicalls.matchListBySummoner
#result = callApi(call,apikey,variables,myversion,myregion)
print((result.values())['id'])
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20,long(time.time()))
queue = CrawlerQueue()
queue.add(queueEl)
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20,long(time.time()))
queue.add(queueEl)
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20,long(time.time()))
queue.add(queueEl)
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20,long(time.time()))
queue.add(queueEl)
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20,long(time.time()))
queue.add(queueEl)
queueEl = CrawlerElement("Summoner",(result.values()[0])['id'],20,long(time.time()))
queue.add(queueEl)
el = queue.pop()
print(el._score)
print(el._id)
print(el._elem)
"""""

