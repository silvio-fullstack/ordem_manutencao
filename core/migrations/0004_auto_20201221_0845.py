# Generated by Django 3.1.4 on 2020-12-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ordem_abertura_servico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem',
            name='Abertura_servico',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]