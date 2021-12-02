from django import forms
from .models import Lawyer

class EditorForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    specialty = forms.CharField(max_length=100, required=True)
    address = forms.CharField(max_length=100, required = True)
    phone = forms.CharField(max_length=100, required = True)
    email = forms.EmailField(max_length=100, required = True)
    license = forms.CharField(max_length=100, required = True)
    rating = forms.IntegerField(max_length=10, required = True)
    #cost = forms.IntegerField()
    #comment = forms.ForeignKey(Review, blank=True, null=True, on_delete=forms.CASCADE)
    #image = forms.ImageField(upload_to='images/')
    website = forms.URLField(max_length=200)
    #guests = forms.ManyToManyField(Guests, blank=True)