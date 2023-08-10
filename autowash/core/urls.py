from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('collapse/', views.collapse, name='collapse'),
    path('fitting/', views.fitting, name='fitting'), 
    path('locksmith/', views.locksmith, name='locksmith'),
    path('allservices/', views.allServices, name='allservices'),
    path('wash/', views.wash, name='wash'),
]