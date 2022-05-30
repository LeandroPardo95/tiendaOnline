from email.policy import default
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)
    detail = models.CharField(max_length=250, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class meta:
        verbose_name = 'Categoria'
        verbose_plural_name = 'Categorias'


class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='Nombre')
    detail = models.CharField(max_length=250, verbose_name='Detalle', blank=True, null=True)
    price = models.FloatField(verbose_name='Precio')
    stock = models.FloatField(verbose_name='Cantidad')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # MediaFiles
    image = models.ImageField(blank=True, null=True, upload_to='tienda/productos') # agregar default
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class meta:
        verbose_name = 'Producto'
        verbose_plural_name = 'Productos'
    
    def __str__(self):
        return "{} - ${}".format(self.name, self.price)
