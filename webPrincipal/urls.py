"""tienda URL Configuration

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
from django.urls import path
from .views import IndexView

from django.conf import settings #para importar las imagenes de servicios desde el panel adm
from django.conf.urls.static import static # tambien para las imagenes desde el panel de adm

app_name = 'landingApp'

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    
]

# https://docs.djangoproject.com/en/4.0/howto/static-files/
# TAMBIEN PARA MOSTRAR LAS IMAGENES DESDE EL PANEL DE ADM
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
