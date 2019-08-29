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
        takeApi = requests.get('https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=RGAPI-1101085a-49ff-457c-a039-884e2e63935f')
        apiDict = takeApi.json()
        summonerLevel = apiDict['summonerLevel']
        return render(request,'level.html', {'summonerName': summonerName, 'summonerLevel': summonerLevel})
