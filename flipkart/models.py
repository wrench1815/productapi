from django.db import models

from mobile import models as MobileModels
from productimage import models as ProductImageModel


class Vendor(models.Model):
    """Model definition for Vendor."""

    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Vendor."""

        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        """Unicode representation of Vendor."""
        return '{}'.format(self.name)


class Brand(models.Model):
    """Model definition for Brand."""

    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Brand."""

        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        """Unicode representation of Brand."""
        return '{}'.format(self.name)


class Specification(models.Model):
    """Model definition for Specification."""

    general = models.ForeignKey(MobileModels.General,
                                related_name='specification',
                                on_delete=models.CASCADE)
    display = models.ForeignKey(MobileModels.Display,
                                related_name='specification',
                                on_delete=models.CASCADE)
    memory = models.ForeignKey(MobileModels.Memory,
                               related_name='specification',
                               on_delete=models.CASCADE)
    camera = models.ForeignKey(MobileModels.Camera,
                               related_name='specification',
                               on_delete=models.CASCADE)
    video_recording = models.ForeignKey(MobileModels.VideoRecording,
                                        related_name='specification',
                                        on_delete=models.CASCADE)
    connectivity = models.ForeignKey(MobileModels.Connectivity,
                                     related_name='specification',
                                     on_delete=models.CASCADE)
    os = models.ForeignKey(MobileModels.Os,
                           related_name='specification',
                           on_delete=models.CASCADE)
    processor = models.ForeignKey(MobileModels.Processor,
                                  related_name='specification',
                                  on_delete=models.CASCADE)
    battery = models.ForeignKey(MobileModels.Battery,
                                related_name='specification',
                                on_delete=models.CASCADE)
    sound = models.ForeignKey(MobileModels.Sound,
                              related_name='specification',
                              on_delete=models.CASCADE)
    body = models.ForeignKey(MobileModels.Body,
                             related_name='specification',
                             on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Specification."""

        verbose_name = 'Specification'
        verbose_name_plural = 'Specifications'

    def __str__(self):
        """Unicode representation of Specification."""
        return 'General:{}, Display:{}, Memory:{}, Camera:{}, Video Recording:{}, Connectivity:{}, OS:{}, Processor:{}, Battery:{}, Sound:{}, Body:{}'.format(
            self.general, self.display, self.memory, self.camera,
            self.video_recording, self.connectivity, self.os, self.processor,
            self.battery, self.sound, self.body)


class Availability(models.Model):
    """Model definition for Availability."""

    upcoming = models.BooleanField(default=False)
    upcoming_date = models.DateField(null=True, blank=True)
    out_of_stock = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Availability."""

        verbose_name = 'Availability'
        verbose_name_plural = 'Availability'

    def __str__(self):
        """Unicode representation of Availability."""
        return 'upcoming: {} out of stock: {}'.format(self.upcoming,
                                                      self.out_of_stock)


class Mobile(models.Model):
    """Model definition for Mobile."""

    name = models.TextField()
    price = models.FloatField()
    discount = models.FloatField()
    color = models.CharField(max_length=255)
    product_images = models.ForeignKey(ProductImageModel.ProductImage,
                                       on_delete=models.CASCADE,
                                       related_name='mobile')
    url = models.URLField(blank=True, null=True)
    availability = models.ForeignKey('Availability',
                                     on_delete=models.CASCADE,
                                     related_name='mobile')

    # related fields
    specifications = models.OneToOneField(Specification,
                                          related_name='mobile',
                                          on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand',
                              related_name='mobile',
                              on_delete=models.CASCADE)
    vendor = models.ForeignKey('Vendor',
                               related_name='mobile',
                               on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Mobile."""

        verbose_name = 'Mobile'
        verbose_name_plural = 'Mobiles'

    def __str__(self):
        """Unicode representation of Mobile."""
        return 'name: {}, price: {}'.format(self.name, self.price)
