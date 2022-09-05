from django.shortcuts import render, redirect
from .forms import PalavraForm
from .models import Palavra


# Create your views here.
def home(request):
    return render(request, 'index.html')


def cadastro(request):
    palavras = Palavra.objects.all()
    if request.method == 'POST':
        form = PalavraForm(request.POST, request.FILES)
        if form.is_valid():
            print('eh valido')
            form.save()
            return redirect('cadastro')
    else:
        form = PalavraForm()
    return render(request, 'cadastro.html', {'form': form,'palavras': palavras})


def imprimir(request):
    return render(request, 'imprimir.html')


def escrever(request):
    return render(request, 'escrever.html')
