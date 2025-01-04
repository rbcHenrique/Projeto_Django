from django.shortcuts import render

''' 
Aqui colocamos as funções que estão no parâmetro path, que esta no arquivo urls.py do app usuário 

path('login', login, name='login'),
path('cadastro', cadastro, name='cadastro'),
'''

def login(request):
    return render(request, 'usuarios/login.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')