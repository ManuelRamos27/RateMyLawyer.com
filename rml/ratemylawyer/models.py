from django.db import models

# Create your models here.
class Lawyer(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    license = models.CharField(max_length=100)
    rating = models.IntegerField(max_length=10)
    cost = models.IntegerField()
    comment = models.ForeignKey(Review, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    website = models.URLField(max_length=200)
    guests = models.ManyToManyField(Guests, blank=True)
    
    def __str__(self):
        return self.name