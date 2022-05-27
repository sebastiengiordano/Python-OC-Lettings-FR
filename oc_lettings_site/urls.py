from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
