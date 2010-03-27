# Create your views here.
from categorias.models import Categoria
from django.shortcuts import render_to_response
def principal(request):
    return render_to_response('principal/index.html',
                              {'categorias':Categoria.objects.all()})