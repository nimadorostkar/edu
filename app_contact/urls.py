from django.urls import path, re_path
from app_contact import views




urlpatterns = [
    path('support', views.support, name='support'),
    path('about', views.about, name='about'),
]
