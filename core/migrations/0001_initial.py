# Generated by Django 3.1.4 on 2020-12-11 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now=True)),
                ('update', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('Nome', models.CharField(max_length=50, verbose_name='Nome do Manutentor')),
                ('funcao', models.CharField(choices=[('eletric', 'Eletricista'), ('macanic', 'Mecânico'), ('lub', 'Lubrificador'), ('aut', 'Automação'), ('refri', 'Refrigeração'), ('aux_eletric', 'Auxiliar Eletricista'), ('aux_mecanic', 'Auxiliar Mecânico'), ('aux_refri', 'Auxiliar Refrigeração')], default='eletric', max_length=25, verbose_name='Função do Manutentor')),
            ],
            bases=('core.base',),
        ),
    ]
