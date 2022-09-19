from django import forms

from .models import Teams

class TeamCreationFrom(forms.ModelForm):
    class Meta:
        model = Teams
        fields = "__all__"