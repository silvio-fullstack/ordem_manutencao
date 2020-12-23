from django.shortcuts import render, redirect
from .models import (
    Manutencao, 
    Equipamentos, 
    Ordem, 
    Almoxarifado,
)
from .forms import (
    ManutencaoForm, 
    EquipamentosForm, 
    OrdemForm, 
    FecharOrdemForm, 
    AbrirOrdemForm, 
    OrdemConsultarForm, 
    AlmoxarifadoForm, 
    AbrirOrdemForm,
)
from datetime import datetime
from django.contrib import messages

# --- VIEWS DOS MANUTENTORES ------------------------
def manutentor(request):
    dados = Manutencao.objects.all()
    context = {
        'dados': dados,
    }
    return render(request, 'ordem/manutentor.html', context)


def manutentor_add(request):
    if request.method == 'POST':
        form = ManutencaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manutencao')
    form = ManutencaoForm()
    context = {
        'form': form,
    }
    return render(request, 'ordem/manutentor_add.html', context)

def manutentor_update(request, id):
    dados = Manutencao.objects.get(id=id)
    form = ManutencaoForm(request.POST or None, instance=dados)
    context = {
        'form': form,
        'dados': dados,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('manutencao')
    else:
        return render(request, 'ordem/manutentor_update.html', context)


def manutentor_delete(request, id):
    dados = Manutencao.objects.get(id=id)

    if request.method == 'POST':
        dados.delete()
        return redirect('manutencao')
    else:
        return render(request, 'ordem/manutentor_delete.html', {'dados': dados})


# ----- VIEWS DO EQUIPAMENTOS

def equipamentos(request):
    dados = Equipamentos.objects.all()
    context = {
        'dados': dados,
    }
    return render(request, 'ordem/equipamento.html', context)


def equipamentos_add(request):
    if request.method == 'POST':
        form = EquipamentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipamento')
    form = EquipamentosForm()
    context = {
        'form': form,
    }
    return render(request, 'ordem/equipamento_add.html', context)

def equipamentos_update(request, id):
    dados = Equipamentos.objects.get(id=id)
    form = EquipamentosForm(request.POST or None, instance=dados)
    context = {
        'dados': dados,
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('equipamento')
    else:
        return render(request, 'ordem/equipamento_update.html', context)


def equipamentos_delete(request, id):
    dados = Equipamentos.objects.get(id=id)

    if request.method == 'POST':
        dados.delete()
        return redirect('equipamento')
    else:
        return render(request, 'ordem/equipamento_delete.html', {'dados': dados})

#--- VIEWS ---- ORDEM DE SERVICO ----------------------------------------------

def ordem(request):
    dados = Ordem.objects.all()
    context = {
        'dados': dados,
    }
    return render(request, 'ordem/ordem.html', context)


def ordem_add(request):
    dados = Ordem.objects.all()
    form = OrdemForm()
    context = {
        'dados': dados,
        'form': form,
    }
    if request.method == 'POST':
        form = OrdemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ordem')

    return render(request, 'ordem/ordem_add.html', context)


def ordem_visualizar(request, id):
    dados = Ordem.objects.get(id=id)
    almox = Almoxarifado.objects.all()
    form = OrdemConsultarForm(request.POST or None, instance=dados)
    context = {
        'dados': dados,
        'form': form,
        'almox': almox,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ordem')
    else:
        return render(request, 'ordem/ordem_consultar.html', context)   

def ordem_salvar(request, id):
    dados = Ordem.objects.get(id=id)
    almox = Almoxarifado.objects.all()
    form = OrdemConsultarForm(request.POST or None, instance=dados)
    context = {
        'dados': dados,
        'form': form,
        'almox': almox,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ordem')
            messages.success(request, 'DEU CERTO')
    else:
        return render(request, 'ordem/ordem_visualizar.html', context)   


def ordem_fechar(request, id):
    dados = Ordem.objects.get(id=id)
    almox = Almoxarifado.objects.all()
    form = FecharOrdemForm(request.POST or None, instance=dados)
    context = {
        'dados': dados,
        'form': form,
        'almox': almox,
    }

    if request.method == 'POST':
        now = datetime.now()
        dados.Situacao = 'concluido'
        dados.Estado = 'Funcionando'
        dados.Termino_servico = now
        if form.is_valid():
            form.save()
            return redirect('ordem')
    else:
        return render(request, 'ordem/ordem_fechar.html', context)


def ordem_abrir(request, id):
    dados = Ordem.objects.get(id=id)
    form = AbrirOrdemForm(request.POST or None, instance=dados)
    context = {
        'dados': dados,
        'form': form,
    }

    if request.method == 'POST':
        now = datetime.now()
        dados.Situacao = 'atendimento'
        dados.Inicio_servico = now
        if form.is_valid():
            form.save()
            return redirect('ordem')
    else:
        return render(request, 'ordem/ordem_abrir.html', context)


def ordem_update(request, id):
    dados = Ordem.objects.get(id=id)
    form = OrdemForm(request.POST or None, instance=dados)
    context = {
        'dados': dados,
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ordem')
    else:
        return render(request, 'ordem/ordem_update.html', context)


def ordem_delete(request, id):
    dados = Ordem.objects.get(id=id)

    if request.method == 'POST':
        dados.delete()
        return redirect('ordem')
    else:
        return render(request, 'ordem/ordem_delete.html', {'dados': dados})

def ordem_consultar(request, id):
    dados = Ordem.objects.get(id=id)
    form = OrdemConsultarForm(request.POST or None, instance=dados)
    context = {
        'dados': dados,
        'form': form,
    }

    return render(request, 'ordem/ordem_consultar.html', context)


#------ VIEWS do Almoxarifado ----------------------------


def almoxarifado(request):
    dados = Almoxarifado.objects.all()
    context = {
        'dados': dados,
    }
    return render(request, 'ordem/almoxarifado.html', context)


def almoxarifado_add(request):
    if request.method == 'POST':
        form = AlmoxarifadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('almoxarifado')
    form = AlmoxarifadoForm()
    context = {
        'form': form,
    }
    return render(request, 'ordem/almoxarifado_add.html', context)

def almoxarifado_update(request, id):
    dados = Almoxarifado.objects.get(id=id)
    form = AlmoxarifadoForm(request.POST or None, instance=dados)
    context = {
        'dados': dados,
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('almoxarifado')
    else:
        return render(request, 'ordem/almoxarifado_update.html', context)


def almoxarifado_delete(request, id):
    dados = Almoxarifado.objects.get(id=id)

    if request.method == 'POST':
        dados.delete()
        return redirect('almoxarifado')
    else:
        return render(request, 'ordem/almoxarifado_delete.html', {'dados': dados})


def adicionar_peca(request):
    form = AlmoxarifadoForm(request.POST)
    return render(request, 'ordem/adicionar_peca.html', {'form': form})