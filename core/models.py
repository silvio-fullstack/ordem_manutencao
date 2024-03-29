from django.db import models
from django.contrib.auth.models import User

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

class Almoxarifado(Base):
    Peca = models.CharField(max_length=50, help_text="Nome da Peça")
    Rua = models.CharField(max_length=10, help_text="Rua da Peça")
    Local = models.CharField(max_length=10, help_text="Local da Peça")
    Preco = models.FloatField(max_length=10, help_text="Valor da Peça")
    Qto = models.IntegerField(help_text="Quantidade de Peças em Estoque")
    Minimo = models.IntegerField(help_text="Estoque Minimo")


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
    estado_choices = [
        ('Parado', 'Equipamento Parado'),
        ('Funcionando', 'Equipamento Funcionando'),
    ]
    tipo_choices = [
        ('Corretivo', 'Serviço Corretivo'),
        ('Preventivo', 'Serviço Preventivo'),
        ('Inspecao', 'Serviço de Inpeção'),
        ('Melhoria', 'Serviço de Melhoria'),
    ]

    Modificado = models.DateTimeField(auto_now_add=True)
    Solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
    Equipamento = models.ForeignKey(Equipamentos, on_delete=models.CASCADE)
    Tipo_Servico = models.CharField(
        verbose_name='Tipo do Serviço', 
        max_length=25,
        choices=tipo_choices,
        default='Corretivo',     
    )
    Descricao = models.TextField()
    Obs = models.TextField()
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
    Estado = models.CharField(
        verbose_name='Estado do Equipamento', 
        max_length=25,
        choices=estado_choices,
        default='Parado',
    )
    Abertura_servico = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    Inicio_servico = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    Termino_servico = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    Pecas = models.ManyToManyField(Almoxarifado, blank=True)
    Pecas = models.ManyToManyField(Almoxarifado, null=True, blank=True)


class Book(models.Model):

    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name

class Eventos(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=True)
    data = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    obs = models.TextField()
    po = models.ForeignKey(Ordem, on_delete=models.PROTECT)


class Maquinas(Base):
    Nome = models.ForeignKey(Equipamentos, on_delete=models.PROTECT)
    Ordem = models.CharField(max_length=10, null=True, blank=True)
    estado_choices = [
        ('Parado', 'Equipamento Parado'),
        ('Funcionando', 'Equipamento Funcionando'),
        ('Erro', 'Erro na Leitura'),
    ]
    Estado = models.CharField(
        verbose_name='Estado do Equipamento', 
        max_length=25,
        choices=estado_choices,
    )
