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
from .views import ProductView, Tienda, Operar, carrito, addCart

app_name = 'tiendaApp'

urlpatterns = [
    path('', Tienda.as_view(), name='inicioTienda'),
    path('operar/', Operar.as_view(), name='ApiTienda'),
    path('api/carrito/', carrito, name='carrito'),
    path('api/carrito/add/<int:id>', addCart, name='addCarrito'),

    path('test/', ProductView.as_view(), name='ProductList'),

]
