# Generated by Django 3.1.4 on 2021-09-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210917_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='maquinas',
            name='Ordem',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
