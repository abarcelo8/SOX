"""
URL configuration for socios_rcd_mallorca project.

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
from socios.views import crear_socio, modificar_socio, obtener_socios

urlpatterns = [
    path('crear_socio/', crear_socio, name='crear_socio'),
    path('modificar_socio/<str:dni>/', modificar_socio, name='modificar_socio'),
    path('obtener_socios/', obtener_socios, name='obtener_socios'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]
