import re
from django.shortcuts import render
from .models import Film


# Create your views here.
def index(request):
    films = Film.objects.all()
    return render(request, "index.html", {"films": films})


def moviegrid(request):
    films = Film.objects.all()
    return render(request, "moviegrid.html", {"films": films})


def help(request):
    return render(request, "bloglist.html")
