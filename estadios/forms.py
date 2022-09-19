from django import forms

from .models import Stadiums

class StadiumCreationFrom(forms.ModelForm):
    class Meta:
        model = Stadiums
        fields = "__all__"