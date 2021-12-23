from django.urls import path
from . import views

urlpatterns =[
    #/
    path('', views.main, name="main"),
    # /contact/
    path('contact/', views.contact, name="contact"),
    # /create/
    path('create/', views.create, name="create"),
    # /edit/<int - from lawyer id
    path('edit/<int:lawyer_id>', views.edit, name='edit'),
    # /browselawyer/
    path('browselawyer/', views.browse, name="browse"),
    # /media/
    path('media/', views.media, name="media"),
    # /comment/<int - from lawyer id
    path('comment/<int:lawyer_id>', views.browse_comment, name='browse_comment'),
    

   
]