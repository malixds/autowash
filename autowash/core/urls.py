from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('collapse/', views.collapse, name='collapse'),
    path('fitting/', views.fitting, name='fitting'),
    path('locksmith/', views.locksmith, name='locksmith'),
    path('allservices/', views.allServices, name='allservices'),
    path('wash/', views.wash, name='wash'),
    path('expresswash/', views.expressWash, name='expresswash'),
    path('contacts/', views.contacts, name='contacts'),
    path('photowash/', views.photo_wash, name='photowash'),
    path('photoshop/', views.photo_shop, name='photoshop'),
    path('shop/', views.shop, name='shop'),
    path('euro/', views.euro, name='euro'),
    path('nano/', views.nano, name='nano'),
    path('engine/', views.engine, name='engine'),
    path('interior/', views.interior, name='interior'),
    path('cons/', views.cons, name='cons'),
    path('complexclear/', views.complexClear, name='complexclear'),
    path('diskclear/', views.diskClear, name='diskclear'),
]
