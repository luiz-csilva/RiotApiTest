from django.db import models

# Create your models here.

def summoner():
    summonerName = models.CharField(max_length=255)
    return summonerName