# Generated by Django 2.0 on 2019-06-14 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_auto_20190612_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='createdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
