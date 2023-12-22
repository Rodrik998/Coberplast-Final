from django.db import models

class category(models.Model):
    name = models.CharField(max_length=50, name="nombre")

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

class products (models.Model):
    name = models.CharField(max_length= 200, name="nombre")
    category = models.ForeignKey(category, on_delete=models.SET_NULL, null=True, blank=True)
    cod = models.CharField(max_length=10, name="codigo")
    price = models.FloatField(blank=False, null=False, default=0, name="precio")
    product_image = models.ImageField(upload_to='product_image', blank=True, null=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'