from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.sp_index,name='sp_index'),
]