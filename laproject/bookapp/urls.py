from django.urls import path
from . import views

app_name = 'bookapp'

urlpatterns = [
     path('master/', views.master, name='master'),
     path('registration/', views.registration, name='registration'),
     path('gallery/', views.gallery, name='gallery'),
     path('booking/', views.booking, name='booking')
]
