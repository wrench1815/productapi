from django.contrib import admin

from mobile import models


@admin.register(models.Battery)
class BatteryAdmin(admin.ModelAdmin):
    '''Admin View for Battery'''

    list_display = (
        'battery_type',
        'battery_capacity',
        'stand_by_time',
    )


@admin.register(models.Body)
class BodyAdmin(admin.ModelAdmin):
    '''Admin View for Body'''

    list_display = (
        'body_height',
        'body_width',
        'body_thickness',
    )


@admin.register(models.Camera)
class CameraAdmin(admin.ModelAdmin):
    '''Admin View for Camera'''

    list_display = (
        'rear_camera',
        'rear_camera_flash',
        'front_camera',
    )


@admin.register(models.Connectivity)
class ConnectivityAdmin(admin.ModelAdmin):
    '''Admin View for Connectivity'''

    list_display = (
        'wifi',
        'radio',
        'infrared',
    )


@admin.register(models.Display)
class DisplayAdmin(admin.ModelAdmin):
    '''Admin View for Display'''

    list_display = (
        'screen_size',
        'screen_resolution',
        'display_type',
    )


@admin.register(models.General)
class GeneralAdmin(admin.ModelAdmin):
    '''Admin View for General'''

    list_display = (
        'network',
        'sim_type',
        'dual_sim',
    )


@admin.register(models.Memory)
class MemoryAdmin(admin.ModelAdmin):
    '''Admin View for Memory'''

    list_display = (
        'internal_memory',
        'external_memory',
        'ram',
    )


@admin.register(models.Os)
class OsAdmin(admin.ModelAdmin):
    '''Admin View for Os'''

    list_display = (
        'os',
        'os_version',
    )


@admin.register(models.Processor)
class ProcessorAdmin(admin.ModelAdmin):
    '''Admin View for Processor'''

    list_display = (
        'processor_type',
        'processor_speed',
        'chipset_group',
    )


@admin.register(models.Sound)
class SoundAdmin(admin.ModelAdmin):
    '''Admin View for Sound'''

    list_display = (
        'jack_35mm',
        'loudspeaker',
    )


@admin.register(models.VideoRecording)
class VideoRecordingAdmin(admin.ModelAdmin):
    '''Admin View for VideoRecording'''

    list_display = ('rear_camera_video_quality', )
