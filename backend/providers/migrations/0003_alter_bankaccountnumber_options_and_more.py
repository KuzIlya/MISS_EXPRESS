# Generated by Django 5.0.2 on 2024-08-18 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankaccountnumber',
            options={},
        ),
        migrations.RemoveField(
            model_name='bankaccountnumber',
            name='number',
        ),
    ]
