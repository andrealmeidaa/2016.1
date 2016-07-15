from django.http.request import QueryDict
from django.shortcuts import render,redirect
from django.views.generic.list import ListView #Importa a classe com a ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from appsisprod.forms import *
from appsisprod.models import *
# Create your views here.

def home(request):
    return render(request,'base.html')
def exibirMateriaPrima(request):
    materias=MateriaPrima.objects.all().order_by('descricao')
    dados={'materias':materias}
    return render(request,'exibirMateriaPrima.html',dados)

def exibirProcesso(request):
    processos=Processo.objects.all()
    dados={'processos':processos}
    return render(request,'exibirProcessoProducao.html',dados)
def prestador_list(request):


    nome_busca=request.GET.get('nome_busca') #Recupera um parâmetro passado pela requisição do tipo get

    if (nome_busca): #Se o parâmetro existir, então busca pelo nome que contenha o texto passado
        prestadores_list=PrestadorServico.objects.filter(nome__contains=nome_busca).order_by('nome')
    else: #Caso contrário lista tudo
        prestadores_list = PrestadorServico.objects.all().order_by('nome')
        nome_busca="" #Coloca uma String vazia
    paginator=Paginator(prestadores_list,3)
    page=request.GET.get('page')
    try:
        prestadores = paginator.page(page) #Tenta recuperar uma página normal
    except PageNotAnInteger:
        prestadores = paginator.page(1) #Recupera a primeira página
    except EmptyPage:
        prestadores = paginator.page(paginator.num_pages) #Recupera a última página

    #Retorna a lista, juntamente com a string utilizada, para que permaneça na tela
    #Além disso, retorna as informações para paginação
    dados={'prestadores':prestadores,'nome_busca':nome_busca,'paginator':paginator,'page_obj':prestadores}
    return render(request, 'prestador/prestador_list.html', dados)
def prestador_new(request):
    if (request.method=="POST"):
        form=PrestadorServicoForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('prestador-list')
    else:
        form=PrestadorServicoForm()
    dados={'form':form}
    return render(request,'prestador/prestador_form.html',dados)

def prestador_edit(request,pk):
    prestador=PrestadorServico.objects.get(id=pk) #Consulta o banco de dados
    if (request.method=="POST"): # Se a requisição for do tipo post, executa o código
        form=PrestadorServicoForm(request.POST,instance=prestador) # Cria uma instância do form, usando o objeto selecionado, para preencher os campos e indicando que funciona como um post
        if (form.is_valid()): #Se nenhum problema surgir, salva o código
            form.save()
            return redirect('prestador-list') #Redireciona par a lista de prestadores
    else:
        form=PrestadorServicoForm(instance=prestador) #Executado quando se clica no botão de Atualizar na listagem
        dados={'form':form} #Passa o formulário como informação de contexto
    return render(request,'prestador/prestador_form.html',dados)

def prestador_delete(request):

    if (request.method=="DELETE"):
        pk=int(QueryDict(request.body).get('pk'))#Recupera informação que veio dentro da requisição Ajax
        prestador=PrestadorServico.objects.get(id=pk)
        prestador.delete()
    return redirect('prestador-list')




class CargoView(ListView):
    template_name = 'cargo/cargo_list.html'  #Identifica qual o template vinculado a classe
    model = Cargo #Estabelece qual o modelo será utilizado na view
    #queryset = Cargo.objects.all().order_by('descricao') #Estabelece qual consulta deve gerar os dados. Senão for especificado, usa a consulta padrao objects.all
    paginate_by = 5 #Número de registro por página
    context_object_name = 'cargos' #Nome da variável utilizada dentro do template

    def get_queryset(self): #Trata o query set, ou seja, a definição dos dados
        busca=self.request.GET.get('nome_busca') #Recupera um parâmetro
        if( not busca):
            busca=""
        return self.model.objects.filter(descricao__contains=busca)
    def get_context_data(self,**kwargs): #Trata as informações de contexto
        #**kwargs significa que a função python pode receber um número indefinido de parâmetros
        context=super(CargoView,self).get_context_data(**kwargs)
        busca = self.request.GET.get('nome_busca')
        if (not busca):
            busca = ""
        context['nome_busca']=busca
        return context

class CargoCreateView(CreateView):
    model = Cargo
    template_name = 'cargo/cargo_form.html'
    fields = ['descricao', 'salario']
    success_url = reverse_lazy('cargo-list')
class CargoUpdateView(UpdateView):
    model=Cargo
    template_name = 'cargo/cargo_form.html'
    fields = ['descricao', 'salario']
    success_url = reverse_lazy('cargo-list')
class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'cargo/cargo_delete.html'
    success_url = reverse_lazy('cargo-list')
    def delete(self, request, *args, **kwargs):
        try:
            return super(CargoDeleteView,self).delete(request,*args,**kwargs)
        except models.ProtectedError as error: #Melhorar o formato da resposta de erro
            id=self.kwargs['pk']
            erro='Existem Prestadores de Serviços Vinculados a Este Cargo'
            messages.error(request,erro) #Usa a funcionalidade para envio de mensagens
            return HttpResponseRedirect(reverse('cargo-delete',kwargs={'pk':id}))



