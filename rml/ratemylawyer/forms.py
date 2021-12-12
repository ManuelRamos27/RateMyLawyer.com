from django import forms
from .models import Lawyer
from .models import Specialty

cost_choices = [('$','$'),('$$','$$'),('$$$','$$$'),('$$$$','$$$$')]
star_choices = [('*','*'),('**','**',),('***','***'),('****','****'),('*****','*****')]

class EditorForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    address = forms.CharField(max_length=255, required=True)
    phone = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    license = forms.CharField(max_length=255, required=True)
    #cost = forms.IntegerField()
    website = forms.URLField(max_length=200)
    #rating = forms.IntegerField()
    rating = forms.CharField(label='How many stars would you give this lawyer?', widget=forms.Select(choices=star_choices))
    cost = forms.CharField(label='How would you classify cost?', widget=forms.Select(choices=cost_choices))
    choices = []
    for specialty in Specialty.objects.all():
        choices.append((specialty.specialty_id, specialty.name))
    specialties = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple, required=True)