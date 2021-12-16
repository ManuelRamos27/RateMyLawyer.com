from django.urls import path
from . import views

urlpatterns =[
    #main/
    path('', views.main, name="main"),
    path('contact/', views.contact, name="contact"),
    path('create/<int:lawyer_id>', views.create, name="create"),
    path('edit/<int:lawyer_id>', views.edit, name='edit'),
    path('browselawyer/', views.browse, name="browse"),
    path('media/', views.media, name="media"),
    path('comment/<int:lawyer_id>', views.add_comment_to_post, name='add_comment_to_post'),

   
]