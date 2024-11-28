from django.contrib import admin 
from galeria.models import Fotografia # importar o Model (Tabela do BD) 

class ListandoFotografias(admin.ModelAdmin): # criado classe para configurar a pagina Admin
    list_display = ("id", "nome", "legenda", "publicada") # criado itens do BD mostrados no Admin. Adicionamos o campo publicada na lista de exibição
    list_display_links = ("id", "nome") # criado itens clicáveis
    search_fields = ("nome",) # criado os campos de busca. NÃO ESQUECER DA VÍRGULA (TEM Q SER MAIS DE UM ITEM O CAMPO)
    list_filter = ("categoria",) # criado nova tupla para fazer filtro por tags
    list_editable = ("publicada",) # Incluir como editável, tem relação com o campo "publicada criado em list_display"
    list_per_page = 10 # criada paginação, quantidade de itens que aparece um uma página

admin.site.register(Fotografia, ListandoFotografias) # adicionar aqui todas as classes criadas aqui

