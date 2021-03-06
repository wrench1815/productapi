# Generated by Django 4.0.2 on 2022-02-06 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_alter_connectivity_bluetooth_version_and_more'),
        ('productimage', '0001_initial'),
        ('flipkart', '0003_brand_vendor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upcoming', models.BooleanField(default=False)),
                ('upcoming_date', models.DateField()),
                ('out_of_stock', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Availability',
                'verbose_name_plural': 'Availabilitys',
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('color', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, null=True)),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobile', to='flipkart.availability')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobile', to='flipkart.brand')),
                ('product_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobile', to='productimage.productimage')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.battery')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.body')),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.camera')),
                ('connectivity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.connectivity')),
                ('display', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.display')),
                ('general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.general')),
                ('memory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.memory')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.os')),
                ('processor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.processor')),
                ('sound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.sound')),
                ('video_recording', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='mobile.videorecording')),
            ],
            options={
                'verbose_name': 'Specification',
                'verbose_name_plural': 'Specifications',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='mobile',
            name='specifications',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mobile', to='flipkart.specification'),
        ),
        migrations.AddField(
            model_name='mobile',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobile', to='flipkart.vendor'),
        ),
    ]
