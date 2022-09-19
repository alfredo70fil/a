from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Teams
from .forms import TeamCreationFrom

# Create your views here.

class index(generic.View):
    template_name = "equipos/index.html"

    def get(self, request):
        context = {

        }
        return render(request, "equipos/index.html", context)

class CreateTeams(generic.View):
    template_name = "equipos/create_team.html"
    model = Teams
    form_class = TeamCreationFrom
    success_url = reverse_lazy("teams:teams_list")
    
# list
class TeamsList(generic.View):
    template_name = "equipos/teams_list.html"
    
    def get(self, request, *args, **kwargs):
        querylist = Teams.objects.all()
        context = {
            "teams_list": querylist
        }
        return render(request, self.template_name, context)

# Detail
class TeamsDetail(generic.View):
    template_name = "equipos/teams_detail.html"
    def get(self, request, pk, *args, **kwargs):
        queryset = Teams.objects.get(pk=pk)
        context = {
            "object": queryset
        }
        return render(request, self.template_name, context)

# Update
class TeamsUpdate(generic.View):
    template_name = "equipos/teams_update.html"
    model = Teams
    fields = "__all__"
    sucess_url = reverse_lazy("teams:teams_list")

# Delete
def TeamsDelete(request, pk):
    team = Teams.objects.get(pk=pk, status=True)
    team.status = False
    team.save()
    messages.warning(request, "Se ha eliminado el equipo")
    return redirect("teams:teams_list")