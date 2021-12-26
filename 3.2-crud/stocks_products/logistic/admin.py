from django.contrib import admin

# Register your models here.
from logistic.models import Stock, Product


class ProductAdmin(admin.ModelAdmin):
    pass


class StockAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
