from django.urls import path
from . import views



urlpatterns = [
    # main/
    path('', views.main, name="main"),
    path('contact/', views.contact, name="contact"),
    path('create/<int:post_id>', views.create, name="create"),
    path('edit/<int:post_id>', views.edit, name='edit'),
    

]