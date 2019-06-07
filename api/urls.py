# api/urls.py

""" from .views import DetailsView 

url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),

 """
from django.urls import path
from . import views

urlpatterns = [
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('',  views.Bucketlist, name="Bucketlist"),
    path(r'^bucketlists/(?P<pk>[0-9]+)/$', views.Bucketlist, name="Bucketlist"),
]
