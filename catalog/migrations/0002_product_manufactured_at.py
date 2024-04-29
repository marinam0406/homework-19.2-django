# Generated by Django 5.0.4 on 2024-04-20 20:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='manufactured_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата производства продукта'),
        ),
    ]
