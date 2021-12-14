from django.shortcuts import render
from .models import Lawyer
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EditorForm
# from .models import Datetime



# Create your views here.

# def ratemylawyer(request):
#     if request.method == 'GET':
#         return render(request = request,
#                     template_name = 'main.html')
# main

def main(request):
    return render(request, 'main.html')

def browse(request):
    reviews = Lawyer.objects.all().order_by('-lawyer_id')
    return render(request=request, template_name='browselawyer.html', context={ 'reviews' : reviews})

def create(request, lawyer_id ):
    if request.method == 'GET':
        form = EditorForm()
        return render(request=request, template_name='create.html', context={ 'form': form, 'id': lawyer_id })

    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            if 'create' in request.POST:
                # get cleaned data from form
            
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                address = form.cleaned_data['address']
                phone = form.cleaned_data['phone']
                license = form.cleaned_data['license']
                specialties = form.cleaned_data['specialties']
                cost = form.cleaned_data['cost']
                rating = form.cleaned_data['rating']
                # create QuerySet object with cleaned name, specialty, address, phone
                lawyer = Lawyer.objects.create(name=name, email=email, address=address, phone=phone, license=license, cost=cost, rating=rating)
                # set cleaned tags to ManyRelatedManager object
                lawyer.specialties.set(specialties)
            submit = form.cleaned_data['browse']
        return HttpResponseRedirect(reverse('browse'))

     
     
def contact(request):
    return render(request, 'contact.html')
    if request.method == 'GET':
        return render(request = request,
                      template_name = 'contact.html')

def edit(request):
    return render(request, 'edit.html')
    if request.method == 'GET':
            return render(request = request,
                      template_name = 'edit.html')



def media(request):
    return render(request, 'media.html')
    pass

