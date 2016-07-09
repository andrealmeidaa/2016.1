from django.shortcuts import render
from appsisprod.models import *
# Create your views here.

def home(request):
    return render(request,'base.html')
def exibirMateriaPrima(request):
    materias=MateriaPrima.objects.all().order_by('descricao')
    dados={'materias':materias}
    return render(request,'exibirMateriaPrima.html',dados)
def exibirPrestadores(request):
    prestadores=PrestadorServico.objects.all().order_by('nome')
    dados={'prestadores':prestadores}
    return render(request,'exibirprestador.html',dados)
def exibirProcesso(request):
    processos=Processo.objects.all()
    dados={'processos':processos}
    return render(request,'exibirProcessoProducao.html',dados)
