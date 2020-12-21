from django.forms import ModelForm

from .models import Manutencao, Equipamentos, Ordem


class ManutencaoForm(ModelForm):
    class Meta:
        model = Manutencao
        fields = '__all__'


class EquipamentosForm(ModelForm):
    class Meta:
        model = Equipamentos
        fields = '__all__'

class OrdemForm(ModelForm):
    class Meta:
        model = Ordem
        fields = {
            'Solicitante',
            'Equipamento',
            'Tipo_Servico',
            'Descricao',
            'Setor',
            'Estado',
            }

class FecharOrdemForm(ModelForm):
    class Meta:
        model = Ordem
        fields = {
            'Causa',
            'Manutentor',
            'Realizado',
            'Estado',
        }

class AbrirOrdemForm(ModelForm):
    class Meta:
        model = Ordem
        fields = {
            'Manutentor',
        }

class OrdemConsultarForm(ModelForm):
    class Meta:
        model = Ordem
        fields = '__all__'
