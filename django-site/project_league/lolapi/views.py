from django.shortcuts import render
from .models import Summoner
from django.http import Http404

# Create your views here.

def detail(request, summoner_name):
    try:
        s = Summoner(name = summoner_name)
        s.getSummoner(summoner_name)
    except ValueError:
        raise Http404(summoner_name, " does not exist")
    return render(request, 'detail.html', {'summoner': s})
