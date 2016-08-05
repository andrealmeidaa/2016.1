from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from appvendas.forms import *
from django.forms import formset_factory
from django.http.request import QueryDict
from appvendas.models import *
# Create your views here.

def home(request):
    return render(request,'base.html')


def exibirproduto(request,id_produto):


    produto=Produto.objects.get(id=id_produto)
    return render(request,'exibirproduto.html',{'produto':produto})


def produto_list(request):

    criterio=request.GET.get('criterio')

    if(criterio):
        produtos=Produto.objects.\
            filter(descricao__contains=criterio)
    else:
        produtos = Produto.objects.all().order_by('descricao')
        criterio=""
    dados={'produtos':produtos,'criterio':criterio}
    return render(request, 'produto/produto_list.html', dados)
def produto_new(request):
    if (request.method=="POST"):
        form=ProdutoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('produto_list')
    else:
        form=ProdutoForm()
    dados={'form':form}
    return render(request,'produto/produto_form.html',dados)

def produto_update(request,pk):
    produto=Produto.objects.get(id=pk)
    if (request.method=="POST"):
        form=ProdutoForm(request.POST,instance=produto)
        if(form.is_valid()):
            form.save()
            return redirect('produto_list')
    else:
        form=ProdutoForm(instance=produto)
    dados={'form':form,'produto':produto}
    return render(request,'produto/produto_form.html',dados)
def produto_delete(request,pk):
    produto=Produto.objects.get(id=pk)
    produto.delete()
    return redirect('produto_list')

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
def unidade_detail(request, pk):
    unidade=Unidade.objects.get(id=pk)
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
    return render(request, 'unidade/unidade_form.html', dados)
def unidade_delete(request,pk):
    unidade=Unidade.objects.get(id=pk)
    unidade.delete()
    return redirect('unidade_list')
def venda_list(request):
    vendas=Venda.objects.all()
    lista={'vendas':vendas}
    return render(request, 'venda/venda_list.html', lista)

def venda_new(request):
    if (request.method=="POST"):
        venda_form=VendaForm(request.POST)
        if (venda_form.is_valid()):
            venda=venda_form.save(commit=False)
            venda_formset=VendaFormSet(request.POST,instance=venda)
            if (venda_formset.is_valid() ):
                venda_form.save()
                venda_formset.save()
                return redirect('venda_list')
        else:
            venda_formset=VendaFormSet(request.POST)
    else:
        venda_form=VendaForm()
        venda_formset=VendaFormSet()
    dados={'form_venda':venda_form,'form_venda_produto':venda_formset}
    return render(request,'venda/venda_form.html',dados)

def venda_update(request,pk):
    venda=Venda.objects.get(id=pk)
    if (request.method=="POST"):
        venda_form=VendaForm(request.POST,instance=venda)
        if (venda_form.is_valid()):
            venda=venda_form.save(commit=False)
            venda_formset=VendaFormSet(request.POST,instance=venda)
            if(venda_formset.is_valid()):
                venda_form.save()
                venda_formset.save()
                return redirect('venda_list')
        else:
            venda_formset=VendaFormSet(request.POST,instance=venda)
    else:
        venda_form=VendaForm(instance=venda)
        venda_formset=VendaFormSet(instance=venda)
    dados = {'form_venda': venda_form, 'form_venda_produto': venda_formset,'venda':venda}
    return render(request, 'venda/venda_form.html', dados)
#TODO Implementar a exibição de detalhes da venda
def venda_detail(request,pk):
    pass

def venda_delete(request):
    if (request.method == "DELETE"):
        pk = int(QueryDict(request.body).get('pk'))  # Recupera informação que veio dentro da requisição Ajax
        venda=Venda.objects.get(id=pk)
        venda.delete()
    return redirect('venda_list')
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