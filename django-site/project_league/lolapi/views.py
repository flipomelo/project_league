from django.shortcuts import render
from .models import Summoner

# Create your views here.

def detail(request, summoner_name):
    s = Summoner(name = summoner_name)
    s.getSummoner(summoner_name)
    return render(request, 'detail.html', {'summoner': s})
