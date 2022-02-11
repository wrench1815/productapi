from django.db import models


class ProductImage(models.Model):
    """Model definition for ProductImage."""

    image = models.URLField()

    class Meta:
        """Meta definition for ProductImage."""

        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImages'

    def __str__(self):
        """Unicode representation of ProductImage."""
        return self.image
