# Generated by Django 4.0.2 on 2022-02-09 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productimage', '0001_initial'),
        ('mobile', '0005_alter_general_sim_type'),
        ('amazon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upcoming', models.BooleanField(default=False)),
                ('upcoming_date', models.DateField(blank=True, null=True)),
                ('out_of_stock', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Availability',
                'verbose_name_plural': 'Availability',
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
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_mobile', to='amazon.availability')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_mobile', to='amazon.brand')),
                ('product_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_mobile', to='productimage.productimage')),
            ],
            options={
                'verbose_name': 'Mobile',
                'verbose_name_plural': 'Mobiles',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.battery')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.body')),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.camera')),
                ('connectivity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.connectivity')),
                ('display', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.display')),
                ('general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.general')),
                ('memory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.memory')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.os')),
                ('processor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.processor')),
                ('sound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.sound')),
                ('video_recording', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_specification', to='mobile.videorecording')),
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
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_mobile', to='amazon.specification'),
        ),
        migrations.AddField(
            model_name='mobile',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amazon_mobile', to='amazon.vendor'),
        ),
    ]
