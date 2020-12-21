# Generated by Django 3.1.4 on 2020-12-21 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201221_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almoxarifado',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('Peca', models.CharField(help_text='Nome da Peça', max_length=50)),
                ('Rua', models.CharField(help_text='Rua da Peça', max_length=10)),
                ('Local', models.CharField(help_text='Local da Peça', max_length=10)),
                ('Preco', models.IntegerField(help_text='Valor da Peça', max_length=10)),
            ],
            bases=('core.base',),
        ),
    ]
