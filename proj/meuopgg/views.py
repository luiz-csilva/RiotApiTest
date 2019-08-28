from django.shortcuts import render
import requests
from .models import summoner

# Create your views here.

def index(request):
    return render(request,'index.html')

def level(request):
    if request.method == 'POST':
        invocador = summoner()
        summonerName = invocador.summonerName = request.POST.get('summonerName')
        region = request.POST.get('region')
        takeApi = requests.get('https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=RGAPI-4eac7039-7560-4fae-9c4e-a58facd6e2a1')
        apiDict = takeApi.json()
        summonerLevel = apiDict['summonerLevel']
        return render(request,'level.html', {'summonerName': summonerName, 'summonerLevel': summonerLevel})
