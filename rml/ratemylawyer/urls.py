from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns = [
    # main/
    path('', views.main, name="main"),
    path('contact/', views.contact, name="contact"),
    path('create/<int:specialty_id>', views.create, name="create"),
    path('edit/<int:specialty_id>', views.edit, name='edit'),
    path('browselawyer/', views.browse, name="browse"),
<<<<<<< HEAD

]
=======
    path('media/', views.media, name="media"),   
]
>>>>>>> 842c9c9307d705ce836af5f95c5a205cd6e4ebde
