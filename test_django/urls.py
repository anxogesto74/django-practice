"""test_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from test_django.views import hello_world, hello_name, bucles, cargadores_1, cargadores_2, plantilla_incrustada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world),
    path('hello_name', hello_name),
    path('bucles/', bucles),
    path('cargadores_1/', cargadores_1),
    path('cargadores_2/', cargadores_2),
    path('plantilla_incrustada/', plantilla_incrustada),
]
