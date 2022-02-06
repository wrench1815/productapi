from django.contrib import admin
from . import models


@admin.register(models.Mobile)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Mobile'''

    list_display = ('name', 'price')


@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):
    '''Admin View for Vendor'''

    list_display = ('name', )


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    '''Admin View for Brand'''

    list_display = ('name', )


@admin.register(models.Specification)
class BrandAdmin(admin.ModelAdmin):
    '''Admin View for Specification'''

    # list_display = ('general', )


@admin.register(models.Availability)
class BrandAdmin(admin.ModelAdmin):
    '''Admin View for Availability'''

    list_display = (
        'upcoming',
        'upcoming_date',
    )
