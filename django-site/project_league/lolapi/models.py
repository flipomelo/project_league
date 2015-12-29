from django.db import models
import json

# Create your models here.
class Summoner(models.Model):
    """Maps to Riot API summoner DTO.
    Also contains timestamp for when object was last updated.
    """
    summoner_id = models.BigIntegerField(primary_key=True)
    # Names "should" be 16 chars, but sometimes we get weird names (ex. "IS141dca1d0484dcf8adc09")
    name = models.CharField(max_length=24)
    std_name = models.CharField(max_length=24)  # This is `name` as lowercase with spaces stripped.
    profile_icon_id = models.IntegerField()
    revision_date = models.BigIntegerField()
    summoner_level = models.IntegerField()  # 'long' in DTO, but we know it's <= 30
    region = models.CharField(max_length=4)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
            return self.name + " - LVL " + str(self.summoner_level)

    def __str__(self):
        return self.name + " - LVL " + str(self.summoner_level)

    def getSummoner(self, summoner_name):
        return "woehoe!"

    def parseJson(self, json):
        for key in json.keys():
            self.summoner_id = json[key]['id']
            self.name = json[key]['name']
            self.std_name = json[key]['name']
            self.summoner_level = json[key]['summonerLevel']

        return self
