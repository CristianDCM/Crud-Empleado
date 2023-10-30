from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'inicio_app'
urlpatterns = [
    path('', views.InicioTemplateView.as_view(), name='InicioTemplateView'),
]