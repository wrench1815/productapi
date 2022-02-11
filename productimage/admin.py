from django.contrib import admin

from . import models


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    '''Admin View for ProductImage'''

    # list_display = ('url', )
