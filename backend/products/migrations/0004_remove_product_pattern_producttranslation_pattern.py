# Generated by Django 5.0.2 on 2024-08-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_options_remove_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pattern',
        ),
        migrations.AddField(
            model_name='producttranslation',
            name='pattern',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Узор товара'),
        ),
    ]
