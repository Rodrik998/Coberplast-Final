from django.contrib import admin

from Products.models import products, category

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from Products.models import products, category


@admin.register(products)
class product_admin(admin.ModelAdmin):
    list_display = ('nombre','codigo','precio')

@admin.register(category)
class category_admin(admin.ModelAdmin):
    list_display = ('nombre',)

class ProductResource(resources.ModelResource):
    class Meta:
        model = products
        import_id_field = ["cod"]
        skip_unchanged = True
        use_bulk = True


class CategoryResource(resources.ModelResource):
    class Meta:
        model = category
        import_id_fields = ["name"]