from django.db import models


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(max_length=100)
    short_description = models.TextField()
    long_decription = models.TextField()
    price = models.FloatField()
    discount = models.FloatField()
    image = models.URLField()
    brand = models.CharField(max_length=100)
    url = models.URLField()
    stock = models.IntegerField()
    vendor = models.CharField(max_length=100)

    # relatted fields
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
