# -*- encoding:utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('all/', views.pizza_list, name='Pizza List'),
]
