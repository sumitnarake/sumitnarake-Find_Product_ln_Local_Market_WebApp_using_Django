# Generated by Django 4.1.3 on 2023-05-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_product_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=None, upload_to='product_images/'),
        ),
    ]