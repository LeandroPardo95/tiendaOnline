
import json

from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Product
from .carro import Carro
# Create your views here.


# *********************************** CONFIG JSON **********************

# Cambiar nombre a productos y ordenar.
class Operar(View):

    # esto es para saltar el csrf token, no es correcto pero esta solo de prueba.
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    # fin de salto de csrf token
    
    def get(self, request):
        productos = list(Product.objects.values()) # paso muy importante para poder parsaarlo a JSON

        datos = {'message':'Success', 'Productos':productos}

        return JsonResponse(datos)
    

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)

        Product.objects.create(
            name = jd['name'],
            detail = jd['detail'],
            price = jd['price'],
            stock = jd['stock'],
            category_id = jd['category_id'],
            image = jd['image'],
        )

        datos = {'message':'Success', 'Producto': jd}

        return JsonResponse(datos)

# *********************************** FIN JSON **********************

class Tienda(TemplateView):
    template_name = 'index.html'



# revisar
# aca probar una clase view, con en el constructor tenga el request
# No lo pude hacer con View, leer documentacion (session id)
def carrito(request):
    carro=Carro(request)

    prod_carro = request.session['carro'].items()

    productos = []

    for key,value in request.session['carro'].items():
        productos.append(value)
        
    datos = {'message':'success', 'productos':productos}

    
    return JsonResponse(datos)

def addCart(request, id):
    # tienda/api/carrito/add/<int:id>
    carro = Carro(request)
    prod = Product.objects.get(id=id)
    carro.add_Prod(prod)

    # Resonse
    jd = Product.objects.values().filter(id=id)
    res = {'message':'Success', 'Producto':[list(jd)]}

    return JsonResponse(res)



# ----------------------- VISTAS BASADAS EN CLASES ------------------------
# ---------------------------- TEST ---------------------------------------
class ProductView(ListView):
    model = Product
    paginate_by: 5
    template_name = 'test.html'

