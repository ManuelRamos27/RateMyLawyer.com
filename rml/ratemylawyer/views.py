from django.shortcuts import render, get_object_or_404, redirect
from .models import Lawyer
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EditorForm, CommentForm
# from .models import Datetime



# Create your views here.

def main(request):
    return render(request, 'main.html')

def browse(request):
    reviews = Lawyer.objects.all().order_by('-lawyer_id')
    return render(request=request, template_name='browselawyer.html', context={ 'reviews' : reviews})

def create(request,):
    if request.method == 'GET':
        form = EditorForm()
        return render(request=request, template_name='create.html', context={ 'form': form })

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
                website = form.cleaned_data['website']
                # create QuerySet object with cleaned name, specialty, address, phone
                lawyer = Lawyer.objects.create(name=name, email=email, address=address, phone=phone, license=license, cost=cost, rating=rating, website=website)
                # set cleaned tags to ManyRelatedManager object
                lawyer.specialties.set(specialties)
            #submit = form.cleaned_data['browse']
        return HttpResponseRedirect(reverse('browse'))

     
     
def contact(request):
    return render(request, 'contact.html')
    if request.method == 'GET':
        return render(request = request,
                      template_name = 'contact.html')

def edit(request, lawyer_id):
    if request.method == 'GET':
        # get Lawyer object by it's lawyer_id
        post = Lawyer.objects.get(pk=lawyer_id)
        specialids = []
        for tag in post.specialties.all():
            specialids.append(tag.specialty_id)
        form = EditorForm(initial={'name' : post.name, 'address' : post.address, 'phone' : post.phone, 'email' : post.email, 'license' : post.license, 'specialids': specialids, 'cost' : post.cost, 'rating' : post.rating, 'website' : post.website })
        return render(request=request, template_name='edit.html', context={'form' : form, 'id': lawyer_id})
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
                if 'save' in request.POST:
                    name = form.cleaned_data['name']
                    email = form.cleaned_data['email']
                    address = form.cleaned_data['address']
                    phone = form.cleaned_data['phone']
                    license =  form.cleaned_data['license']
                    specialids = form.cleaned_data['specialties']
                    cost = form.cleaned_data['cost']
                    rating = form.cleaned_data['rating']
                    website = form.cleaned_data['website']
                    posts = Lawyer.objects.filter(pk=lawyer_id)
                    posts.update(name=name, address=address, email=email, phone=phone, license=license, cost=cost, rating=rating, website=website)
                    posts[0].specialties.set(specialids)
                elif 'delete' in request.POST:
                    Lawyer.objects.filter(pk=lawyer_id).delete()
        return HttpResponseRedirect(reverse('browse'))






def media(request):
    return render(request, 'media.html')
    pass

def add_comment_to_post(request, lawyer_id):
    post = get_object_or_404(Lawyer, lawyer_id = lawyer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('browse', lawyer_id=post.lawyer_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})