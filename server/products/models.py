from django.db import models


DEFAULT_IMG = '../static/product/img/default.png'


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'

    name = models.CharField(
        verbose_name='Наименование категории',
        max_length=255,
        unique=True)
    description = models.CharField(
        verbose_name='Описание категории',
        max_length=500,
        blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='category')
    name = models.CharField(
        verbose_name='Наименование продукта',
        max_length=128)
    short_description = models.CharField(
        verbose_name='Краткое описание продукта',
        max_length=300,
        blank=True)
    description = models.TextField(
        verbose_name='Описание продукта',
        blank=True)
    specifications = models.TextField(
        verbose_name='Характеристики продукта',
        blank=True)
    price_now = models.DecimalField(
        verbose_name='Текущая цена продукта',
        max_digits=8,
        decimal_places=2,
        default=0)
    price_old = models.DecimalField(
        verbose_name='Предыдущая цена продукта',
        max_digits=8,
        decimal_places=2,
        default=0)
    quantity = models.PositiveIntegerField(
        verbose_name='Количество на складе',
        default=0)
    image = models.ImageField(
        upload_to='products_images',
        default=DEFAULT_IMG,
        blank=True)
    status = models.CharField(
        verbose_name='Статус продукта',
        max_length=50,
        blank=True)

    def __str__(self):
        return f"​{self.name}​ (​{self.category.name}​)"
