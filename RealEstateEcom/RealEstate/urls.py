from unicodedata import name
from django.urls import path
from RealEstate import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
]
