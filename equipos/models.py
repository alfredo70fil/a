from django.db import models

# Create your models here.

class Teams(models.Model):
    numberteam = models.IntegerField(primary_key=True)
    nameTeam = models.CharField(max_length=32, default="Generic Team", null=False, blank=False)
    city = models.CharField(max_length=18, default="Generic City", null=False, blank=False)
    numberPlayers = models.IntegerField(default=0, null=False, blank=False)
    mascotname = models.CharField(max_length=32, default="Generic Mascot", null=False, blank=False)
    logo = models.ImageField(upload_to="equipos/", blank=True, null=True)
    motto = models.CharField(max_length=200, default="Without motto", null=False, blank=False)
    dateForge = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.nameTeam