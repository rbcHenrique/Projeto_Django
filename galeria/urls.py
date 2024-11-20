# No APP vamos importar a função index do views

from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
        path('', index),
        path('imagem/', imagem, name = 'imagem'),
]