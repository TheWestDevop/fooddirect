# Generated by Django 2.0 on 2019-06-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_auto_20190612_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='product_image/'),
        ),
    ]
