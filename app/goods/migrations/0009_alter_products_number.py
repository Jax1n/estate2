# Generated by Django 5.0.4 on 2024-05-20 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_products_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='number',
            field=models.CharField(max_length=150, verbose_name='Номер'),
        ),
    ]
