from datetime import date
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    images = models.ImageField(upload_to='goods_images', unique=True,blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    location = models.CharField(max_length=150, verbose_name='Местоположение')
    number = models.CharField(max_length=150, verbose_name='Номер')
    date = models.DateField(default=date.today, verbose_name='Дата')
    rooms = models.CharField(max_length=150, verbose_name='Количество комнат')
    furnish = models.CharField(max_length=150, verbose_name='Мебель')
    status = models.CharField(max_length=150, verbose_name='Состояние')
    bedroom = models.CharField(max_length=150, verbose_name='Спальня')
    bathroom = models.CharField(max_length=150, verbose_name='Ванная')
    balcony = models.CharField(max_length=150, verbose_name='Балкон')
    documents = models.CharField(max_length=150, verbose_name='Документы')
    # age = models.CharField(max_length=150, verbose_name='Срок')
    is_featured = models.BooleanField(default=False)
    floors = models.CharField(max_length=150, verbose_name='Количество этажей')
    square = models.CharField(max_length=150, verbose_name='Площадь')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)