from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Players
from .forms import PlayersCreationFrom

# Create your views here.
class index(generic.View):
    template_name = "jugadores/index.html"

    def get(self, request):
        context = {

        }
        return render(request, "jugadores/index.html", context)

class CreatePlayer(generic.View):
    template_name = "jugadores/create_player.html"
    model = Players
    form_class = PlayersCreationFrom
    success_url = reverse_lazy("emp:players_list")
    
# list
class PlayersList(generic.View):
    template_name = "estadios/players_list.html"
    
    def get(self, request, *args, **kwargs):
        querylist = Players.objects.all()
        context = {
            "Players_list": querylist
        }
        return render(request, self.template_name, context)

# Detail
class PlayersDetail(generic.View):
    template_name = "estadios/player_detail.html"
    def get(self, request, pk, *args, **kwargs):
        queryset = Players.objects.get(pk=pk)
        context = {
            "object": queryset
        }
        return render(request, self.template_name, context)

# Update
class PlayersUpdate(generic.View):
    template_name = "estadios/player_update.html"
    model = Players
    fields = "__all__"
    sucess_url = reverse_lazy("players:players_list")

# Delete
def PlayerDelete(request, pk):
    team = Players.objects.get(pk=pk, status=True)
    team.status = False
    team.save()
    messages.warning(request, "Se ha eliminado el jugador")
    return redirect("players:players_list")