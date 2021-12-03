from django.contrib import admin
from .models import Lawyer, Specialty

# Register your models here.
admin.site.register(Lawyer)
admin.site.register(Specialty)