from django.db import models
from django.db.models.fields.related import RelatedField


class Vendor(models.Model):
    """Model definition for Vendor."""

    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Vendor."""

        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        """Unicode representation of Vendor."""
        return self.name


class Brand(models.Model):
    """Model definition for Brand."""

    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Brand."""

        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        """Unicode representation of Brand."""
        return self.name


class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(max_length=100)
    short_description = models.TextField()
    long_description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField()
    image = models.URLField()
    url = models.URLField()
    stock = models.IntegerField()

    # related fields
    brand = models.ForeignKey('Brand',
                              related_name='products',
                              on_delete=models.CASCADE)
    vendor = models.ForeignKey('Vendor',
                               related_name='products',
                               on_delete=models.CASCADE)
    category = models.ForeignKey('Category',
                                 related_name='products',
                                 on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
