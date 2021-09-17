# Generated by Django 3.1.4 on 2021-09-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_maquinas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maquinas',
            old_name='nome',
            new_name='Nome',
        ),
        migrations.RemoveField(
            model_name='maquinas',
            name='estado',
        ),
        migrations.AddField(
            model_name='maquinas',
            name='Estado',
            field=models.CharField(choices=[('Parado', 'Equipamento Parado'), ('Funcionando', 'Equipamento Funcionando'), ('Erro', 'Erro na Leitura')], default=1, max_length=25, verbose_name='Estado do Equipamento'),
            preserve_default=False,
        ),
    ]
