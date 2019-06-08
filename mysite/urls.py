from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', include('blog.urls')),
    path('api/', include('article.urls')),
    path('', include('pages.urls')),
    path('index', include('pages.urls')),
]
