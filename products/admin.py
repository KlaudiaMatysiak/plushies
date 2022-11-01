from django.contrib import admin
from .models import Product, Category, Size


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'size',
        'color',
        'price',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
