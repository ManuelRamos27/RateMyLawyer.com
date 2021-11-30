from django.urls import path
from ratemylawyer import main

urlpatterns = [
    path('', main, name="main")
]