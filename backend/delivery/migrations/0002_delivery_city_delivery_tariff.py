# Generated by Django 5.0.2 on 2024-08-16 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='delivery.city', verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='delivery',
            name='tariff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='delivery.tariff', verbose_name='Тариф доставки'),
            preserve_default=False,
        ),
    ]
