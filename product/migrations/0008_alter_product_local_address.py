# Generated by Django 4.1.3 on 2023-05-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_local_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='local_address',
            field=models.CharField(max_length=100),
        ),
    ]
