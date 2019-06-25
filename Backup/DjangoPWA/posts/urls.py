from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.index,name='index'),
    path(r'about',views.about_layout,name='about_layout'),
    path(r'base_layout',views.base_layout,name='base_layout'),
    path(r'getdata',views.getdata,name='getdata'),
    path(r'new', views.post_new, name='post_new'),
    path(r'feed_upload', views.feed_upload, name='feed_upload'),
    
]