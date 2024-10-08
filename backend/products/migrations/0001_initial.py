# Generated by Django 5.0.2 on 2024-08-16 17:05

from decimal import Decimal

import django.core.validators
import django.db.models.deletion
import mptt.fields
import parler.models
from django.db import migrations, models

import mssite.storages


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_components', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(blank=True, null=True, storage=mssite.storages.OverwriteStorage(), upload_to='product_images/', verbose_name='Файл изображения')),
                ('position', models.IntegerField(verbose_name='Позиция изображения')),
            ],
            options={
                'verbose_name': 'Изображение товара',
                'verbose_name_plural': 'Изображения товаров',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Количество товара для выбранного цвета')),
            ],
            options={
                'verbose_name': 'Цвет товара',
                'verbose_name_plural': 'Цвета товаров',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Количество товара для выбранного размера')),
            ],
            options={
                'verbose_name': 'Размер товара',
                'verbose_name_plural': 'Размеры товаров',
            },
        ),
        migrations.CreateModel(
            name='ProductStatusChangeArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_status', models.CharField(choices=[('A', 'Active'), ('B', 'Bin')], verbose_name='Старый статус')),
                ('new_status', models.CharField(choices=[('A', 'Active'), ('B', 'Bin')], verbose_name='Новый статус')),
                ('changed_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время изменения статуса')),
            ],
            options={
                'verbose_name': 'Архив изменений статуса товара',
                'verbose_name_plural': 'Архив изменений статуса товаров',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание товара')),
                ('compound', models.TextField(blank=True, null=True, verbose_name='Состав товара')),
            ],
            options={
                'verbose_name': 'Перевод товара',
                'verbose_name_plural': 'Переводы товаров',
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_number', models.CharField(max_length=9, unique=True, verbose_name='Артикул')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0'), message='Цена не может быть отрицательной')], verbose_name='Цена комплекта')),
                ('season', models.CharField(blank=True, choices=[('Summer', 'Summer'), ('Autumn', 'Autumn'), ('Winter', 'Winter'), ('Spring', 'Spring'), ('Demi-season', 'Demi-season')], null=True, verbose_name='Сезон для ношения')),
                ('pattern', models.CharField(blank=True, max_length=50, null=True, verbose_name='Узор товара')),
                ('mold', models.CharField(choices=[('Oversize', 'Oversize'), ('Slim', 'Slim'), ('Skinny', 'Skinny'), ('Normal', 'Normal'), ('No-mold', 'No-mold')], default='No-mold', verbose_name='Лекало')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Вес товара')),
                ('slug', models.SlugField(blank=True, max_length=1024, unique=True, verbose_name='Слаг товара')),
                ('is_famous', models.BooleanField(default=False, verbose_name='Известный товар')),
                ('status', models.CharField(choices=[('A', 'Active'), ('B', 'Bin')], default='A', verbose_name='Статус проверки модерацией')),
                ('date_and_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')),
                ('category', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_components.category', verbose_name='Категория товаров')),
                ('manufacturerCountry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_components.manufacturercountry', verbose_name='Страна производителя товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-slug'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
    ]
