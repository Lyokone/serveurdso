from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    return render(request, 'landingpage/index.html')

def telechargement(request):
    return render(request, 'landingpage/telechargement.html')

def fonctionnalites(request):
    return render(request, 'landingpage/fonctionnalites.html')
