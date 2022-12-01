from django.shortcuts import render
# Create your views here.

def paginaInicial(request):
    return render(request, 'library/home.html')

def cadastro(request):
    context = {}
    if request.method== "POST":
        erro = {}
        title = request.POST.get('title', None)
        author = request.POST.get('author', None)
        publishingCompany = request.POST.get('publishingCompany', None)
        state = request.POST.get('state', None)
        releaseYear = request.POST.get('releaseYear', None)
        pages = request.POST.get('pages', None)
        print("Informações obtidas no beck-end")

        # Tentando verificar erro de campo em branco
        #if title != "":
        #    erro['title'] = "O campo não pode estar em branco"
        #if author != "":
        #    erro['author'] = "O campo não pode estar em branco"
            
    return render(request, 'library/cadastro.html', context=context)

def lista(request):
    #print(request.get)
    return render(request, 'library/lista.html')


# bookID
# title
# author
# releaseYear
# state
# pages
# publishingCompany
# createAt
