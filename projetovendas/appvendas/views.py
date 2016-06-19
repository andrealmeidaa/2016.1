from django.shortcuts import render
from django.http import HttpResponse
from appvendas.models import *
# Create your views here.

def home(request):
    return render(request,'base.html')
def exibirproduto(request,id_produto):
    produto=Produto.objects.get(id=id_produto)
    return render(request,'exibirproduto.html',{'produto':produto})
def listarprodutos(request):
    produtos=Produto.objects.all().order_by('descricao')
    lista={'produtos':produtos}
    return render(request,'produtos.html',lista)
def listarunidades(request):
    unidades=Unidade.objects.all().order_by('descricao')
    lista={'unidades':unidades}
    return render(request,'unidades.html',lista)
def exibirunidade(request,id_unidade):
    unidade=Unidade.objects.get(id=id_unidade)
    return render(request,'exibirunidade.html',{'unidade':unidade})
def listarvendas(request):
    vendas=Venda.objects.all()
    lista={'vendas':vendas}
    return render(request,'vendas.html',lista)
def listarclientes(request):
    clientes=Cliente.objects.all().order_by('nome')
    lista={'clientes':clientes}
    return render(request,'clientes.html',lista)
def exibircliente(request,idcliente):
    cliente=Cliente.objects.get(id=idcliente)
    contexto={'cliente':cliente}
    return render(request,'exibircliente.html',contexto)
def listarcargos(request):
    cargos=Cargo.objects.all().order_by('descricao')
    lista={'cargos':cargos}
    return render(request,'cargos.html',lista)
def listarfuncionrios(request):
    funcionarios=Funcionario.objects.all().order_by('nome')
    lista={'funcionarios':funcionarios}
    return render(request,'funcionarios.html',lista)
def exibirfuncionario(request,idfuncionario):
    funcionario=Funcionario.objects.get(id=idfuncionario)
    contexto={'funcionario':funcionario}
    return render(request,'exibirfuncionario.html',contexto)