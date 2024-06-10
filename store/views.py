from django.shortcuts import render
from django.contrib.auth.models import User, auth
from home.models import Film


# Create your views here.
def single(request, movie_name):
    films = Film.objects.filter(name=movie_name).first
    context = {"films": films}
    return render(request, "moviesingle.html", context)
