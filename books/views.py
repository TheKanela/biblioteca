from django.shortcuts import render

# Create your views here.

def paginaInicial(request):
    return render(request, 'library/home.html')
def cadastro(request):
    return render(request, 'library/cadastro.html')
def lista(request):
    return render(request, 'library/lista.html')