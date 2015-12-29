from django.shortcuts import render
from .models import Summoner

# Create your views here.

def detail(request, summoner_name):
    Summoner.getSummoner(summoner_name)
    return render(request, 'lolapi/detail.html', {'summoner': summoner})
