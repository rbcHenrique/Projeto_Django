from django.shortcuts import render
from galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404 # criado o get


def index (request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render (request, 'galeria/index.html', {'cards': fotografias})
     # O Index é responável por exibir na página, todos os objetos Fotografia criado, que seria um card inserido na tela.
     # Alterado essa linha com a função filter e o parâmetro publicada=True, só irá publicar as fotos com essa opção ativada. 
     # Alterado com order_by para ordenar as imagens exibidas na order da data da postagem.

def imagem(request, numero_da_foto): # criado o numero_da_foto
    fotografia = get_object_or_404(Fotografia, pk = numero_da_foto) # armazenado a PK em fotografia
    return render(request, 'galeria/imagem.html', {"objeto_capturado": fotografia}) # inserido o valor da variável fotografia em objeto_capturado

def buscar(request):
    todos_os_objetos = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    if "palavra_no_input" in request.GET: # A grande questão aqui, se resumo ai fato de que, 
        # quando estamos escrevendo em um INPUT estamos manipulando a URL, e assim sendo, 
        # manipulamos o que vai aparecer nela, no caso, vai aparecer PALAVRA_NO_INPUT.
        pesquisa_digitada = request.GET['palavra_no_input']
       
        if pesquisa_digitada: 
            todos_os_objetos = todos_os_objetos.filter(nome__icontains= pesquisa_digitada) # Esse parâmetro encontra relação entre a palavra pesquisada e o titulo dos objetos (imagens do site)
    
    return render(request, "galeria/buscar.html", {"cards": todos_os_objetos})