from django.contrib import admin
from .models import Lawyer, Specialty, Comment

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

# Registering the models
admin.site.register(Specialty)
admin.site.register(Lawyer, PostAdmin)