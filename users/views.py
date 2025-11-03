from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PersonForm
# Views for users app will be stored here

def home(request):
    return HttpResponse("Home")
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users")
    else:
        form = PersonForm()
        return render(request,"create_person.html",{"form":form})
            