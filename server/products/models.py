from django.db import models


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'

    name = models.CharField(
        verbose_name='Наименование категории',
        max_length=255,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание категории',
        max_length=500,
        blank=True
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    category = models.ForeignKey(
        ProductCategory,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        related_name='category'
    )
    name = models.CharField(
        verbose_name='Наименование',
        max_length=128
    )
    short_description = models.CharField(
        verbose_name='Краткое описание',
        max_length=1000,
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    specifications = models.TextField(
        verbose_name='Характеристики',
        blank=True
    )
    price_now = models.DecimalField(
        verbose_name='Текущая цена',
        max_digits=8,
        decimal_places=2,
        default=0
    )
    price_old = models.DecimalField(
        verbose_name='Предыдущая цена',
        max_digits=8,
        decimal_places=2,
        default=0
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество на складе',
        default=0
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True
    )
    status = models.CharField(
        verbose_name='Статус продукта',
        max_length=50,
        blank=True
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
    )

    def __str__(self):
        return f"​{self.name}​ (​{self.category.name}​)"
