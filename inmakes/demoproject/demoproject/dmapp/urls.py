from django.urls import path

from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('/', views.home, name='home'),
    path('/', views.about, name='about')
]
