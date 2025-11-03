from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Views for users app will be stored here

def home(request):
    return HttpResponse("Home")
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())