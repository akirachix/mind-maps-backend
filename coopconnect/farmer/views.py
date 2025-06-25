from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def farmer_home(request):
    return HttpResponse("Welcome to the Farmer Page!")