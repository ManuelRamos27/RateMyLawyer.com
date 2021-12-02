from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from . import forms


# Create your views here.

def main(request):
    return render(request=request, template_name='main.html')