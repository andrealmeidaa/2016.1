from django.shortcuts import render
from django.views.generic.list import ListView #Importa a classe com a ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.contrib import messages
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
    template_name = 'cargos/cargos_list.html'  #Identifica qual o template vinculado a classe
    model = Cargo #Estabelece qual o modelo será utilizado na view
    queryset = Cargo.objects.all().order_by('descricao') #Estabelece qual consulta deve gerar os dados. Senão for especificado, usa a consulta padrao objects.all
    paginate_by = 5 #Número de registro por página
    context_object_name = 'cargos' #Nome da variável utilizada dentro do template
class CargoCreateView(CreateView):
    model = Cargo
    template_name = 'cargos/cargos_form.html'
    fields = ['descricao', 'salario']
    success_url = reverse_lazy('cargos')
class CargoUpdateView(UpdateView):
    model=Cargo
    template_name = 'cargos/cargos_form.html'
    fields = ['descricao', 'salario']
    success_url = reverse_lazy('cargos')
class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'cargos/cargos_delete.html'
    success_url = reverse_lazy('cargos')
    def delete(self, request, *args, **kwargs):
        try:
            return super(CargoDeleteView,self).delete(request,*args,**kwargs)
        except models.ProtectedError as error: #Melhorar o formato da resposta de erro
            id=self.kwargs['pk']
            erro='Existem Prestadores de Serviços Vinculados a Este Cargo'
            messages.error(request,erro)
            return HttpResponseRedirect(reverse('cargos-delete',kwargs={'pk':id}))



