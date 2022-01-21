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
   
    Lawyers_Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Matthew Marinez'}))
    Lawyers_Adrres= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'123 Main St. Los Angeles, CA 90012'}))
    Lawyers_Phone_Number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'(123) 456-7890'}))
    Lawyers_Emails = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'MatthewMartinez@law.com'}))
    Lawyers_License_Number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'(123) 456-789'}))
    Lawyers_Website= forms.CharField( widget=forms.TextInput(attrs={'placeholder':'www.matthewmartinez.com'}))
    # Lawyers_Rating = forms.ChoiceField(choices=star_choices, widget=forms.Select(attrs={'class':'form-control'} ))
    # Lawyers_Cost = forms.ChoiceField(choices=star_choices, widget=forms.Select(attrs={'class':'form-control'} ))
    # name = forms.CharField(max_length=255, required=True)
    # address = forms.CharField(max_length=255, required=True)
    # phone = forms.CharField(max_length=255, required=True)_
    # email = forms.EmailField(max_length=255, required=True)
    # license = forms.CharField(max_length=255, required=True)
    # website = forms.URLField(max_length=200)
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

        

    
