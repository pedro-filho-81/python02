from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ver_produto(request):
    return HttpResponse("Aqui estão os produtos disponíveis.")

def inserir_produto(request):
    return HttpResponse("Produto inserido com sucesso!")        
