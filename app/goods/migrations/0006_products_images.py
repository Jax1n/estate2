# Generated by Django 5.0.4 on 2024-04-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_remove_products_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='images',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to='goods_images', verbose_name='Изображение'),
        ),
    ]
