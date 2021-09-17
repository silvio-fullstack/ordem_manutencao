from django.contrib import admin
from .models import Manutencao, AbrirOrdem, Ordem, Book, Eventos, Maquinas

# Register your models here.
admin.site.register(Manutencao)
admin.site.register(AbrirOrdem)
admin.site.register(Ordem)
admin.site.register(Book)
admin.site.register(Eventos)
admin.site.register(Maquinas)
