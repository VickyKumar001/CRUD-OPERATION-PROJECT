from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path("home/", home, name='home'),
    path('add/', add,name='add'),
    path('delete/<int:roll>', delete, name="delete"),
    path('update/<int:roll>', update, name="update"),
    path('doupdate/<int:roll>', doupdate, name="doupdate"),
]
