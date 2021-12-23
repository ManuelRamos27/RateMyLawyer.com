from django import forms 
from django.forms import ModelForm
from .models import Lawyer
from django.core.exceptions import ValidationError
from .models import Specialty, Comment

# Creating lists to be used as options for cost and ratings
cost_choices = [('$','$'),('$$','$$'),('$$$','$$$'),('$$$$','$$$$')]
star_choices = [('*','*'),('**','**',),('***','***'),('****','****'),('*****','*****')]

# Creating form for individual lawyer reviews
class LawyerForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    address = forms.CharField(max_length=255, required=True)
    phone = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    license = forms.CharField(max_length=255, required=True)
    website = forms.URLField(max_length=200)
    rating = forms.CharField(label='How many stars would you give this lawyer?', widget=forms.Select(choices=star_choices))
    cost = forms.CharField(label='How would you classify cost?', widget=forms.Select(choices=cost_choices))
    choices = []
    for specialty in Specialty.objects.all():
        choices.append((specialty.specialty_id, specialty.name))
    specialties = forms.MultipleChoiceField(label = "Specialties: Select the appropriate specialty below", choices=choices, widget=forms.CheckboxSelectMultiple, required=True)

# Comment Form to be used to create new comments once functionable
class CommentForm(forms.Form):
    author = forms.CharField(max_length=20)
    text = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return f"{self.text} by {self.author}"

        

    
