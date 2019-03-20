# Generated by Django 2.1.7 on 2019-03-20 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование продукта')),
                ('short_description', models.CharField(blank=True, max_length=300, verbose_name='Краткое описание продукта')),
                ('description', models.TextField(blank=True, verbose_name='Описание продукта')),
                ('specifications', models.CharField(blank=True, max_length=300, verbose_name='Характеристики продукта')),
                ('price_now', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Текущая цена продукта')),
                ('price_old', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Предыдущая цена продукта')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество на складе')),
                ('image', models.ImageField(blank=True, default='../static/product/img/default.png', upload_to='products_images')),
                ('status', models.TextField(blank=True, verbose_name='Статус продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Наименование категории')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория продуктов',
                'verbose_name_plural': 'Категории продуктов',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.ProductCategory'),
        ),
    ]