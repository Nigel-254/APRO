from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('published/', views.published, name='published cases'),
    path('administration/', views.administration, name='administration'),
    path('report/', views.report, name='report missing person'),
    path('found', views.found, name='found cases'),
    path('administration/messages/', views.message, name='administration messages'),
    path('administration/edit/<int:id>/', views.edit, name='edit' ),
    path('administration/delete/<int:id>/', views.delete, name='delete'),
]