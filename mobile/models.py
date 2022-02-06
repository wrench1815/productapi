from django.db import models


class General(models.Model):
    """Model definition for General."""

    SIM_TYPES = {
        ('Micro-Sim', 'Micro-Sim'),
        ('Nano-Sim', 'Nano-Sim'),
    }

    network = models.TextField()
    sim_type = models.CharField(max_length=10,
                                choices=SIM_TYPES,
                                default='Micro-Sim')
    dual_sim = models.BooleanField(default=True)
    touch_screen = models.BooleanField(default=True)
    fingerprint_unlock = models.BooleanField(default=True)
    face_lock = models.BooleanField(default=True)

    class Meta:
        """Meta definition for General."""

        verbose_name = 'General'
        verbose_name_plural = 'General'

    def __str__(self):
        """Unicode representation of General."""
        return str(self.network)


class Display(models.Model):
    """Model definition for Display."""

    screen_size = models.CharField(max_length=255)
    screen_resolution = models.CharField(max_length=255)
    display_type = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Display."""

        verbose_name = 'Display'
        verbose_name_plural = 'Display'

    def __str__(self):
        """Unicode representation of Display."""
        return str(self.screen_size)


class Memory(models.Model):
    """Model definition for Memory."""

    internal_memory = models.FloatField()
    external_memory = models.FloatField()
    ram = models.FloatField()

    class Meta:
        """Meta definition for Memory."""

        verbose_name = 'Memory'
        verbose_name_plural = 'Memory'

    def __str__(self):
        """Unicode representation of Memory."""
        return str(self.internal_memory)


class Camera(models.Model):
    """Model definition for Camera."""

    rear_camera = models.TextField()
    rear_camera_flash = models.BooleanField(default=True)
    front_camera = models.TextField()
    front_camera_flash = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Camera."""

        verbose_name = 'Camera'
        verbose_name_plural = 'Camera'

    def __str__(self):
        """Unicode representation of Camera."""
        return str(self.rear_camera)


class VideoRecording(models.Model):
    """Model definition for VideoRecording."""

    rear_camera_video_quality = models.TextField()

    class Meta:
        """Meta definition for VideoRecording."""

        verbose_name = 'VideoRecording'
        verbose_name_plural = 'VideoRecording'

    def __str__(self):
        """Unicode representation of VideoRecording."""
        return str(self.rear_camera_video_quality)


class Connectivity(models.Model):
    """Model definition for Connectivity."""

    wifi = models.BooleanField(default=True)
    radio = models.BooleanField(default=True)
    infrared = models.BooleanField(default=True)
    gprs = models.BooleanField(default=True)
    edge = models.BooleanField(default=True)
    nfc = models.BooleanField(default=True)
    usb = models.BooleanField(default=True)
    bluetooth_version = models.FloatField()

    class Meta:
        """Meta definition for Connectivity."""

        verbose_name = 'Connectivity'
        verbose_name_plural = 'Connectivity'

    def __str__(self):
        """Unicode representation of Connectivity."""
        return str(self.wifi)


class Os(models.Model):
    """Model definition for OS."""

    os = models.CharField(max_length=255)
    os_version = models.CharField(max_length=255)

    class Meta:
        """Meta definition for OS."""

        verbose_name = 'OS'
        verbose_name_plural = 'OS'

    def __str__(self):
        """Unicode representation of OS."""
        return str(self.os)


class Processor(models.Model):
    """Model definition for Processor."""

    processor_type = models.CharField(max_length=255)
    processor_speed = models.CharField(max_length=255)
    chipset_group = models.CharField(max_length=255)
    chipset_details = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Processor."""

        verbose_name = 'Processor'
        verbose_name_plural = 'Processor'

    def __str__(self):
        """Unicode representation of Processor."""
        return str(self.processor_type)


class Battery(models.Model):
    """Model definition for Battery."""

    battery_type = models.CharField(max_length=255)
    battery_capacity = models.CharField(max_length=255)
    stand_by_time = models.CharField(max_length=255)
    talktime = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Battery."""

        verbose_name = 'Battery'
        verbose_name_plural = 'Battery'

    def __str__(self):
        """Unicode representation of Battery."""
        return str(self.battery_type)


class Sound(models.Model):
    """Model definition for Sound."""

    jack_35mm = models.BooleanField(default=True)
    loudspeaker = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Sound."""

        verbose_name = 'Sound'
        verbose_name_plural = 'Sound'

    def __str__(self):
        """Unicode representation of Sound."""
        return str(self.jack_35mm)


class Body(models.Model):
    """Model definition for Body."""

    body_height = models.CharField(max_length=255)
    body_width = models.CharField(max_length=255)
    body_thickness = models.CharField(max_length=255)
    body_weight = models.CharField(max_length=255)
    body_type = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Body."""

        verbose_name = 'Body'
        verbose_name_plural = 'Body'

    def __str__(self):
        """Unicode representation of Body."""
        return str(self.body_height)
