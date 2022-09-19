from django.db import models
from django.urls import reverse_lazy
# Create your models here.

class Stadiums(models.Model):
    id = models.IntegerField(primary_key=True)
    nameStadium = models.CharField(max_length=32, default="Generic Stadium", null=False, blank=False)
    city = models.CharField(max_length=18, default="Generic City", null=False, blank=False)
    maxPersons = models.IntegerField(default=0, null=False, blank=False)
    nextGame = models.DateField()

    def __str__(self):
        return self.nameStadium

    def get_absolute_url(self):
        return reverse_lazy('est:stadiums_list')