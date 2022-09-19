from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Stadiums
from .forms import StadiumCreationFrom

# Create your views here.
class index(generic.View):
    template_name = "estadios/index.html"

    def get(self, request):
        context = {

        }
        return render(request, "estadios/index.html", context)

class CreateStadium(generic.View):
    template_name = "estadios/create_stadium.html"
    context = {}
    
    def get_success_message(self, cleaned_data ):
        return "Se ha creado un estadio!"

    def get(self, request, *args, **kwargs):
        form = StadiumCreationFrom()
        self.context = {
            "form": form
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            form = StadiumCreationFrom(request.POST)
            if form.is_valid():
                id = form.cleaned_data.get('id')
                nameStadium = form.cleaned_data.get('nameStadium')
                city = form.cleaned_data.get('city')
                maxPersons = form.cleaned_data.get('maxPersons')
                nextGame = form.cleaned_data.get('nextGame')
                p, created = Stadiums.objects.get_or_create(
                    id=id,
                    nameStadium=nameStadium,
                    city=city,
                    maxPersons=maxPersons,
                    nextGame=nextGame,
                )
                p.save()
                return redirect("/estadios/stadiums_list")
            self.context = {
                "form":form
            }
        return render(request, self.template_name, self.context)

    
# list
class StadiumList(generic.View):
    template_name = "estadios/stadiums_list.html"
    context = {}

    def get(self, request, *args, **kwargs):
        queryset = Stadiums.objects.get_queryset
        self.context = {
            "stadiums": queryset
        }
        return render(request, self.template_name, self.context)


# Detail
def StadiumDetail(request, pk):
    template_name = "estadios/stadium_detail.html"
    context = {
        "stadiums": Stadiums.objects.get(pk=pk)
    }
    return render(request, template_name, context)


# Update
class StadiumUpdate(generic.edit.UpdateView):
    template_name = "estadios/stadium_update.html"
    model = Stadiums
    fields = "__all__"
    sucess_url = "/estadios/stadium_detail"

# Delete
def StadiumsDelete(request, pk):
   # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Stadiums, pk = pk)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "estadios/delete_stadium.html", context)