from django.urls import path
from .views import manutentor, manutentor_add, manutentor_update, manutentor_delete, equipamentos, equipamentos_add, equipamentos_delete, equipamentos_update, ordem, ordem_add, ordem_delete, ordem_update, ordem_fechar, ordem_abrir


urlpatterns = [
    # Manutentores CRUD -------------------------------------------------------------
    path('manutentor/', manutentor, name='manutencao'),
    path('manutentor_add/', manutentor_add, name='manutencao_add'),
    path('manutentor_update/<int:id>', manutentor_update, name='manutentor_update'),
    path('manutentor_delete/<int:id>', manutentor_delete, name='manutentor_delete'),
    # --------------------------------------------------------------------------------
    # Equipamentos CRUD -------------------------------------------------------------
    path('equipamento', equipamentos, name='equipamento'),
    path('equipamento_add', equipamentos_add, name='equipamento_add'),
    path('equipamento_update/<int:id>', equipamentos_update, name='equipamento_update'),
    path('equipamento_delete/<int:id>', equipamentos_delete, name='equipamento_delete'),   
    #--------------------------------------------------------------------------------
    # Ordems CRUD -------------------------------------------------------------
    path('ordem/', ordem, name='ordem'),
    path('ordem_add/', ordem_add, name='ordem_add'),
    path('ordem_update/<int:id>', ordem_update, name='ordem_update'),
    path('ordem_delete/<int:id>', ordem_delete, name='ordem_delete'),  
    path('ordem_fechar/<int:id>', ordem_fechar, name='ordem_fechar'), 
    path('ordem_abrir/<int:id>', ordem_abrir, name='ordem_abrir'), 
]