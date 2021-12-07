from django import forms
from .models import Lawyer
from .models import Specialty

class EditorForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    #specialty = forms.CharField(max_length=255, required=True)
    address = forms.CharField(max_length=255, required=True)
    phone = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    license = forms.CharField(max_length=255, required=True)
    #cost = forms.IntegerField()
    #comment = forms.ForeignKey(Review, blank=True, null=True, on_delete=forms.CASCADE)
    #image = forms.ImageField(upload_to='images/')
    website = forms.URLField(max_length=200)
    #guests = forms.ManyToManyField(Guests, blank=True)
    # specialty = forms.ManyToManyField('Specialty', blank=True)
    choices = []
    for specialty in Specialty.objects.all():
        choices.append((specialty.specialty_id, specialty.name))
    specialties = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple, required=True)