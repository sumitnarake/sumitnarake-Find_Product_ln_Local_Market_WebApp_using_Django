# Generated by Django 4.1.3 on 2023-04-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_shop_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='first_name',
            field=models.TextField(max_length=30),
        ),
    ]