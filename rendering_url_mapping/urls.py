"""
URL configuration for rendering_url_mapping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('karim1/',karim1,name='karim1'),
    path('hasen1/',hasen1,name='hasen1'),
    path('karim2/',karim2,name='karim2'),
    path('hasen2/',hasen2,name='hasen2'),
    path('karim3/',karim3,name='karim3'),
    path('hasen3/',hasen3,name='hasen3'),
    path('karim4/',karim4,name='karim4'),
]
