from django.urls import path
from . import views



urlpatterns = [
    # main/
    path('', views.main, name="main"),
]