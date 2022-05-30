from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name="Home"),
    path("about", views.about, name="about"),
    path("result", views.result, name="results"),
    path("contact", views.contact, name="contact"),
    path("search", views.search, name= "search")
]