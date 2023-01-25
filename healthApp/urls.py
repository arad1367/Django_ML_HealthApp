from django.contrib import admin
from django.urls import path
from . import views

app_name = 'healthApp'
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),   # localhost:8000/healthApp/homepage/
    path('testmodel/', views.testmodel, name='testmodel'),  # localhost:8000/healthApp/testmodel/
    path('about/', views.about, name='about'),
    path('docs/', views.docs, name='docs'),
    path('contacts/', views.contacts, name='contacts'),
]