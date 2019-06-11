from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('article.urls')),    
    path('blog', include('blog.urls')),
    path('index', include('pages.urls')),
    path('posts', include('posts.urls')),
]
