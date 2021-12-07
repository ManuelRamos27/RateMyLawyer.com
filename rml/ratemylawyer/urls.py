from django.urls import path
from . import views



urlpatterns = [
    # main/
    path('', views.main, name="main"),
    path('contact/', views.contact, name="contact"),
    # path('create/<int:specialty_id>', views.create, name="create"),
    # path('edit/<int:specialty_id>', views.edit, name='edit'),
    

]