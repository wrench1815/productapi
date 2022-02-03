from django.contrib import admin
from .models import Product, Category, Vendor, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('name', 'price')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name', 'description')


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    '''Admin View for Vendor'''

    list_display = ('name', )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    '''Admin View for Brand'''

    list_display = ('name', )
