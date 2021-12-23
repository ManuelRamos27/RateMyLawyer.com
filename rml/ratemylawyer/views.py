from django.core.exceptions import TooManyFieldsSent
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Lawyer
from .models import Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LawyerForm, CommentForm
# from .models import Datetime



# Create your views here.

# View for main page of site
def main(request):
    return render(request, 'main.html')

# View to browse all the Lawyer reviews
def browse(request):
    # get QuerySet object containing reviews in descending order of lawyer_id
    reviews = Lawyer.objects.all().order_by('-lawyer_id')
    return render(request=request, template_name='browselawyer.html', context={ 'reviews' : reviews})

def create(request,):
    if request.method == 'GET':
        # assigning Lawyer form from forms to the form variable to be passed to template
        form = LawyerForm()
        return render(request=request, template_name='create.html', context={ 'form': form })

    if request.method == 'POST':
        # Capture POST data as LawyerForm istance
        form = LawyerForm(request.POST)
        # validate form
        if form.is_valid():
            # if form was submitted by clicking create
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
                website = form.cleaned_data['website']
                # create QuerySet object with cleaned name, specialty, address, phone
                lawyer = Lawyer.objects.create(name=name, email=email, address=address, phone=phone, license=license, cost=cost, rating=rating, website=website)
                # set cleaned specialties to ManyRelatedManager object
                lawyer.specialties.set(specialties)
        return HttpResponseRedirect(reverse('browse'))

     
# view for contact page    
def contact(request):
    return render(request, 'contact.html')
    if request.method == 'GET':
        return render(request = request,
                      template_name = 'contact.html')

# view in order to edit existing reviews
def edit(request, lawyer_id):
    if request.method == 'GET':
        # get Lawyer object by it's lawyer_id
        post = Lawyer.objects.get(pk=lawyer_id)
        # get a list of specialty_id from ManyRelatedManager object
        specialids = []
        for specialty in post.specialties.all():
            specialids.append(specialty.specialty_id)
        # pre-populate form with values of the review
        form = LawyerForm(initial={'name' : post.name, 'address' : post.address, 'phone' : post.phone, 'email' : post.email, 'license' : post.license, 'specialids': specialids, 'cost' : post.cost, 'rating' : post.rating, 'website' : post.website })
        return render(request=request, template_name='edit.html', context={'form' : form, 'id': lawyer_id})
    if request.method == 'POST':
        # Capture POST data as LawyerForm instance
        form = LawyerForm(request.POST)
        if form.is_valid():
                # if form was submitted by clicking save
                if 'save' in request.POST:
                    # get cleaned data from form
                    name = form.cleaned_data['name']
                    email = form.cleaned_data['email']
                    address = form.cleaned_data['address']
                    phone = form.cleaned_data['phone']
                    license =  form.cleaned_data['license']
                    specialids = form.cleaned_data['specialties']
                    cost = form.cleaned_data['cost']
                    rating = form.cleaned_data['rating']
                    website = form.cleaned_data['website']
                    # filter Queryset object by lawyer_id
                    posts = Lawyer.objects.filter(pk=lawyer_id)
                    # update Queryset object with cleaned name, address, email, phone, license, cost, rating and website
                    posts.update(name=name, address=address, email=email, phone=phone, license=license, cost=cost, rating=rating, website=website)
                    # set cleaned specialties to ManyRelatedManager object
                    posts[0].specialties.set(specialids)
                # if form was submitted by clicking delete
                elif 'delete' in request.POST:
                    # filter Queryset object by lawyer_id and delete it
                    Lawyer.objects.filter(pk=lawyer_id).delete()
        return HttpResponseRedirect(reverse('browse'))


# view for media page
def media(request):
    return render(request, 'media.html')

# view for seeing comments written for each review
def browse_comment(request, lawyer_id):
    # get Lawyer object by it's lawyer_id
     comments = Lawyer.objects.get(pk=lawyer_id)
     return render(request=request, template_name='browse_comment.html', context={ 'comments' : comments})

