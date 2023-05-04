from django.contrib import admin

from catalogue.models import Brand, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "brand",
        "description",
        "size",
        "gender",
        "type"
    )
    list_filter = ("brand", "gender", "type")


admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)

