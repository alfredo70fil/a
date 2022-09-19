from django.shortcuts import render
from django.views import generic

# Create your views here.
    

class index(generic.View):
    template_name = "home/index.html"

    def get(self, request):
        context = {

        }
        return render(request, "home/index.html", context)
        