from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from appvendas.forms import *
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
def unidade_list(request):
    criterio=request.GET.get('criterio')
    if (criterio):
        unidades=Unidade.objects.filter(descricao__contains=criterio).order_by('descricao')
    else:
        unidades=Unidade.objects.all().order_by('descricao')
        criterio=""
    #Cria o mecanimos de paginação
    paginator=Paginator(unidades,4)
    page=request.GET.get('page')
    try:
        unidades=paginator.page(page)
    except PageNotAnInteger:
        unidades=paginator.page(1)
    except EmptyPage:
        unidades=paginator.page(paginator.num_pages)

    dados={'unidades':unidades,'criterio':criterio,'paginator':paginator,'page_obj':unidades}
    return render(request, 'unidade/unidade_list.html', dados)
def unidade_detail(request, id_unidade):
    unidade=Unidade.objects.get(id=id_unidade)
    return render(request, 'unidade/unidade_detail.html', {'unidade':unidade})
def unidade_new(request):
    if (request.method=="POST"):
        form=UnidadeForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('unidade_list')
    else:
        form=UnidadeForm()
        dados={'form':form}
        return render(request, 'unidade/unidade_form.html', dados)
def unidade_update(request,pk):
    unidade=Unidade.objects.get(id=pk)
    if (request.method=="POST"):
        form=UnidadeForm(request.POST,instance=unidade)
        if (form.is_valid()):
            form.save()
            return redirect('unidade_list')
    else:
        form=UnidadeForm(instance=unidade)
        dados={'form':form}
        return render(request, 'unidade/unidade_list.html', dados)
def unidade_delete(request,pk):
    unidade=Unidade.objects.get(id=pk)
    unidade.delete()
    return redirect('unidade_list')
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