# -*- encoding:utf-8 -*-
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('pizza_app/', include('pizza_app.urls')),
    path('admin/', admin.site.urls),
]
