# Generated by Django 3.1.4 on 2020-12-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201219_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='base',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
