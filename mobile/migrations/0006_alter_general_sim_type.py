# Generated by Django 4.0.2 on 2022-02-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0005_alter_general_sim_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general',
            name='sim_type',
            field=models.CharField(choices=[('Micro-Sim', 'Micro-Sim'), ('Nano-Sim', 'Nano-Sim')], default='Micro-Sim', max_length=10),
        ),
    ]
