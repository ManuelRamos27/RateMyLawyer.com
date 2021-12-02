from django.urls import path
from . import views



urlpatterns = [
    # main/
    path('', main, name="main")
]