from django.urls import path

from . import views


app_name = 'profiles'
urlpatterns = [
    path('profiles/', views.index, name='index'),
    path('profiles/<int:profile_id>/', views.profile, name='profile'),
]
