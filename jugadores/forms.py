from django import forms

from .models import Players

class PlayersCreationFrom(forms.ModelForm):
    class Meta:
        model = Players
        fields = "__all__"