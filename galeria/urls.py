# No APP vamos importar a função index do views

from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
        path('', index, name = 'index'),
        path('imagem/<int:numero_da_foto>', imagem, name='imagem'), # criado o <int:numero_da_foto>
        path('buscar', buscar, name='buscar'),
]