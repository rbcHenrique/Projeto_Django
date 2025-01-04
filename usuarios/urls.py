# atenção aos 3 parâmetros do path 
# 1º é o que aparece na URL
# 2º é o nome da função escrita em views.py do app usuario
# 3º é o que vamos escrever no CDG html para embedar o pyhton. No href por exemplo para direcionar uma página 

from django.urls import path
from usuarios.views import login, cadastro

urlpatterns = [
    path('login', login, name='login_embedar'),
    path('cadastro', cadastro, name='cadastro_embedar'),
]