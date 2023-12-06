from django.contrib import admin

from Products.models import products, category

@admin.register(products)
class product_admin(admin.ModelAdmin):
    list_display = ('nombre','codigo','precio')

@admin.register(category)
class category_admin(admin.ModelAdmin):
    list_display = ('nombre',)