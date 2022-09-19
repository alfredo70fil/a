from django.db import models

from equipos.models import Teams

# Create your models here.

class Players(models.Model):
    numberPlayer = models.IntegerField(primary_key=True)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    namePlayer = models.CharField(max_length=32, default="NAME", null=False, blank=False)
    birthday = models.DateField()
    dateAdd = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.namePlayer