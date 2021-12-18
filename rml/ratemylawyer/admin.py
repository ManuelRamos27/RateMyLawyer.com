from django.contrib import admin
from .models import Lawyer, Specialty, Comment

# Register your models here.
admin.site.register(Lawyer)
admin.site.register(Specialty)
admin.site.register(Comment)