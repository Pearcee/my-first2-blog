from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blank', views.blank, name='blank'),
    path('contact', views.contact, name='contact'),    
]
