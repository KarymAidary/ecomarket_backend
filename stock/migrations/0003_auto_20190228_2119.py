# Generated by Django 2.1.7 on 2019-02-28 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20190218_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
