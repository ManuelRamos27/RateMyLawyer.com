from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime


# Create your views here.

# def ratemylawyer(request):
#     if request.method == 'GET':
#         return render(request = request,
#                     template_name = 'main.html')
# >>>>>>> main
def main(request):
     now = datetime.now()
     current_year = now.year
     return render(request, 'main.html',{'current_year': current_year})
     
     
def contact(request):
    return render(request, 'contact.html')
