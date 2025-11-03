from . import views
from django.urls import path

# app that will contain all the urls to the file

urlpatterns = [
    path("",views.home,name="home")
]