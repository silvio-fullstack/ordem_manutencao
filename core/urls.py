from django.urls import path
from .views import (
    manutentor, 
    manutentor_add, 
    manutentor_update, 
    manutentor_delete, 
    equipamentos, 
    equipamentos_add, 
    equipamentos_delete, 
    equipamentos_update, 
    ordem, ordem_add, 
    ordem_delete, 
    ordem_update, 
    ordem_fechar, 
    ordem_abrir, 
    ordem_consultar, 
    almoxarifado, 
    almoxarifado_add, 
    almoxarifado_delete, 
    almoxarifado_update, 
    adicionar_peca, 
    ordem_salvar, 
    ordem_visualizar,
    maquinas,
    maquinas_add,
    maquinas_update,
    maquinas_delete,
    )
from core.views import MeuView, BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    # -------------------- CLASS BASED VIEWS --------------------------------------
    path('cbv/', MeuView.as_view()),
    path('book/', BookListView.as_view(), name='book-list'),
    path('book/create', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
    # -----------------------------------------------------------------------------
    # Manutentores CRUD -------------------------------------------------------------
    path('manutentor/', manutentor, name='manutencao'),
    path('manutentor_add/', manutentor_add, name='manutencao_add'),
    path('manutentor_update/<int:id>', manutentor_update, name='manutentor_update'),
    path('manutentor_delete/<int:id>', manutentor_delete, name='manutentor_delete'),
    # --------------------------------------------------------------------------------
    # Equipamento CRUD -------------------------------------------------------------
    path('equipamento', equipamentos, name='equipamento'),
    path('equipamento_add', equipamentos_add, name='equipamento_add'),
    path('equipamento_update/<int:id>', equipamentos_update, name='equipamento_update'),
    path('equipamento_delete/<int:id>', equipamentos_delete, name='equipamento_delete'),   
    #--------------------------------------------------------------------------------

    # Maquinas  ------------------------------------------------------------------
    path('maquinas', maquinas, name='maquinas'),
    path('maquinas_add', maquinas_add, name='maquinas_add'),
    path('maquinas_update/<int:id>', maquinas_update, name='maquinas_update'),
    path('maquinas_delete/<int:id>', maquinas_delete, name='maquinas_delete'),   

    # ------------------------------------------------------------------------------
    # Ordems CRUD -------------------------------------------------------------
    path('ordem/', ordem, name='ordem'),
    path('ordem_add/', ordem_add, name='ordem_add'),
    path('ordem_update/<int:id>', ordem_update, name='ordem_update'),
    path('ordem_delete/<int:id>', ordem_delete, name='ordem_delete'),  
    path('ordem_fechar/<int:id>', ordem_fechar, name='ordem_fechar'), 
    path('ordem_abrir/<int:id>', ordem_abrir, name='ordem_abrir'), 
    path('ordem_consultar/<int:id>', ordem_consultar, name='ordem_consultar'),
    path('adicionar_peca', adicionar_peca, name='adicionar_peca'),
    path('ordem_salvar/<int:id>', ordem_salvar, name='ordem_salvar'),
    path('ordem_visualizar/<int:id>', ordem_visualizar, name='ordem_visualizar'),
    #------------------------------------------------------------------------------
    # ALMOXARIFADO CRUD ----------------------------------------------------------
    path('almoxarifado', almoxarifado, name='almoxarifado'),
    path('almoxarifado_add', almoxarifado_add, name='almoxarifado_add'),
    path('almoxarifado_update/<int:id>', almoxarifado_update, name='almoxarifado_update'),
    path('almoxarifado_delete/<int:id>', almoxarifado_delete, name='almoxarifado_delete'),   
]