from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path("", views.index, name='myapp'),
    path("index", views.index, name='index'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
]