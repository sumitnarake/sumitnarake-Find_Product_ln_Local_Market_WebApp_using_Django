# Generated by Django 4.1.3 on 2023-05-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_shop_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='country',
            field=models.CharField(default='india', max_length=50),
        ),
    ]
