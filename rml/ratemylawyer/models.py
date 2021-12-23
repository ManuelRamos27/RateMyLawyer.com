from django.db import models
from django.utils import timezone

# Create your models here.

# Specialty model with a many-to-many relationship to lawyer
class Specialty(models.Model):
    specialty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

# Lawyer model for each specific lawyer review
class Lawyer(models.Model):
    lawyer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    license = models.CharField(max_length=100)
    rating = models.CharField(max_length=6)
    cost = models.CharField(max_length=6)
    website = models.URLField(max_length=200)
    specialties = models.ManyToManyField(Specialty)

    def __str__(self):
        return self.name
        

# Comment model with a one-to-many relationship with Lawyer
class Comment(models.Model):
    post = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='display_comment')
    author = models.CharField(max_length=200)
    text = models.TextField() #body
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text
   