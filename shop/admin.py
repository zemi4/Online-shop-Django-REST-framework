from django.contrib import admin
from .models import Category, Product, Brand


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}   # автозаполнение slug


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Brand, BrandAdmin)
