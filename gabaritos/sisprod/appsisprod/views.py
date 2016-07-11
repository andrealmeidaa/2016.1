from django.shortcuts import render
from django.views.generic.list import ListView #Importa a classe com a ListView
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
class CargoView(ListView):
    template_name = 'cargo_lista.html' #Identifica qual o template vinculado a classe
    model = Cargo #Estabelece qual o modelo será utilizado na view
    queryset = Cargo.objects.all().order_by('descricao') #Estabelece qual consulta deve gerar os dados. Senão for especificado, usa a consulta padrao objects.all
    paginate_by = 5 #Número de registro por página
    context_object_name = 'cargos' #Nome da variável utilizada dentro do template

