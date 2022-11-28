from django.contrib import admin
from farmacia.models import Cliente

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Cliente, Clientes)