from django.db import models

class Base(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Manutencao(Base):
    funcao_choices = [
        ('eletric', 'Eletricista'),
        ('macanic', 'Mecânico'),
        ('lub', 'Lubrificador'),
        ('aut', 'Automação'),
        ('refri', 'Refrigeração'),
        ('aux_eletric', 'Auxiliar Eletricista'),
        ('aux_mecanic', 'Auxiliar Mecânico'),
        ('aux_refri', 'Auxiliar Refrigeração'),
    ]
    Nome = models.CharField(verbose_name='Nome do Manutentor', max_length=50)
    funcao = models.CharField(
        verbose_name='Função do Manutentor', 
        max_length=25,
        choices=funcao_choices,
        default='eletric',
        )
    def __str__(self):
        return self.Nome

class Equipamentos(Base):
    Nome = models.CharField(max_length=50, help_text='Nome do Equipamento')
    Setor = models.CharField(max_length=50, help_text='Setor do Equipamento')
    Fabricante = models.CharField(max_length=50, help_text='Fabricante do Equipamento')
    def __str__(self):
        return self.Nome

class AbrirOrdem(models.Model):
    funcao_choices = [
        ('concluido', 'Serviço Concluido'),
        ('andamento', 'Serviço em Andamento'),
        ('cancelado', 'Serviço Cancelado'),
        ('suspenso', 'Serviço Suspenso'),
        ('aguardando', 'Arguardando Manutenção'),
        ('peca', 'Aguardando Peça'),
    ]
    create = models.DateTimeField(auto_now_add=True)
    Solicitante = models.CharField(max_length=50, help_text='Solicitante da Ordem')
    Equipamento = models.ForeignKey(Equipamentos, on_delete=models.CASCADE)
    Tipo_Servico = models.CharField(max_length=50, help_text='Tipo do Serviço')
    Descricao = models.TextField()
    Setor = models.CharField(max_length=50, help_text='Setor do Serviço')
    Situacao = models.CharField(
        verbose_name='Situação do Serviço', 
        max_length=25,
        choices=funcao_choices,
        default='aguardando',
    )

class Ordem(models.Model):
    funcao_choices = [
        ('concluido', 'Serviço Concluido'),
        ('andamento', 'Serviço em Andamento'),
        ('cancelado', 'Serviço Cancelado'),
        ('suspenso', 'Serviço Suspenso'),
        ('aguardando', 'Arguardando Manutenção'),
        ('peca', 'Aguardando Peça'),
        ('atendimento', 'Em Atendimento'),
    ]
    Modificado = models.DateTimeField(auto_now=True)
    Solicitante = models.CharField(max_length=50, help_text='Solicitante da Ordem')
    Equipamento = models.ForeignKey(Equipamentos, on_delete=models.CASCADE)
    Tipo_Servico = models.CharField(max_length=50, help_text='Tipo do Serviço')
    Descricao = models.TextField()
    Setor = models.CharField(max_length=50, help_text='Setor do Serviço')
    Causa = models.TextField(help_text='Causa do Problema', null=True, blank=True)
    Realizado = models.TextField(help_text='Serviço Realizado', null=True, blank=True)
    Manutentor = models.ForeignKey(Manutencao, on_delete=models.CASCADE, null=True, blank=True)
    Situacao = models.CharField(
        verbose_name='Situação do Serviço', 
        max_length=25,
        choices=funcao_choices,
        default='aguardando',
    )
   