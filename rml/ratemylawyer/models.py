from django.db import models

# Create your models here.

class Specialty(models.Model):
    specialty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Lawyer(models.Model):
    lawyer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    license = models.CharField(max_length=100)
    rating = models.IntegerField()
    cost = models.IntegerField()
    website = models.URLField(max_length=200)
    specialties = models.ManyToManyField(Specialty)

    def __str__(self):
        return self.name
        
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    lawyer_id = models.ForeignKey(Lawyer, on_delete=models.CASCADE)