from django.shortcuts import render
from galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404 # criado o get


def index (request):
    fotografias = Fotografia.objects.all()
    return render (request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, numero_da_foto): # criado o numero_da_foto
    fotografia = get_object_or_404(Fotografia, pk = numero_da_foto) # criado fotografia 
    return render(request, 'galeria/imagem.html', {"objeto_capturado": fotografia}) # criado objeto_capturado