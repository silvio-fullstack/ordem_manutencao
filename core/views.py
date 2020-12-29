from django.shortcuts import render, redirect
from .models import Manutencao, Equipamentos, Ordem, Almoxarifado
from .forms import ManutencaoForm, EquipamentosForm, OrdemForm, FecharOrdemForm, AbrirOrdemForm, OrdemConsultarForm, AlmoxarifadoForm, AbrirOrdemForm, UpdateForm
from datetime import datetime
from django.contrib.auth.models import User
from .models import (
    Manutencao, 
    Equipamentos, 
    Ordem, 
    Almoxarifado,
    Book,
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
from django.views.generic import TemplateView, View, ListView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.edit import CreateView

from django.views.generic.detail import DetailView

from django.views.generic.edit import UpdateView

from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# ----- CLASS BASED VIEWS --------------------------
class MeuView(ListView):
    model = Ordem
    template_name = 'ordem/cbv.html'

@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    template_name = 'book/create.html'
    fields = ('name', 'isbn_number', )
    success_url = reverse_lazy('book-list')


@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):

    model = Book
    template_name = 'book/detail.html'
    context_object_name = 'book'

@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):

    model = Book
    template_name = 'book/update.html'
    context_object_name = 'book'
    fields = ('name', 'isbn_number',)

    def get_success_url(self):
        return reverse_lazy('book-detail', kwargs={'pk': self.object.id})

@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_url = reverse_lazy('book-list')



# --------------------------------------------------

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
    usuario = User.objects.all()
    print(f'Valor do Dados.Manutencao é {usuario}')
    form = AbrirOrdemForm(request.POST or None, instance=dados)
    context = {
        'dados': dados,
        'form': form,

    }

    if request.method == 'POST':
        now = datetime.now()
        if form.is_valid():
            form.save()

        valor = dados.Manutentor
        print(f'O valor e {valor}')
        if valor != None:
            dados.Situacao = 'atendimento'
            dados.Inicio_servico = now
            form.save()

        return redirect('ordem')
    else:
        return render(request, 'ordem/ordem_abrir.html', context)

def ordem_update(request, id):
    dados = Ordem.objects.get(id=id)
    almox = Almoxarifado.objects.all()
    form = UpdateForm(request.POST or None, instance=dados)
    context = {
        'dados': dados,
        'form': form,
        'almox': almox,

    }

    if request.method == 'POST' and '_save' in request.POST:
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


#---- TRSTANDO CRUD EM CLASS BASED VIEWS ---------------------
    
@method_decorator(login_required, name='dispatch')
class BookListView(ListView):

    model = Book
    template_name = 'book/list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        return context
