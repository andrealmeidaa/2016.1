from django.forms import ModelForm,DateInput
from django.forms.models import inlineformset_factory

from appvendas.models import *
class UnidadeForm(ModelForm):
   class Meta:
       model=Unidade
       fields=('descricao','sigla')
       error_messages={
           'descricao':{'required':'Informe a Descrição'},
           'sigla':{'required':'Informe a Sigla'},
       }

class ProdutoForm(ModelForm):
    class Meta:
        model=Produto
        fields=('descricao','unidade','valorUnitario')

class ClienteForm(ModelForm):
    class Meta:
        model=Cliente
        fields=('nome','email','telefone','endereco')

class FuncionarioForm(ModelForm):
	class Meta:
		model = Funcionario
		fields=('nome', 'matricula', 'cargo', 'telefone', 'email')

class CargoForm(ModelForm):
  class Meta:
    model = Cargo
    fields=('descricao',)


class VendaForm(ModelForm):
    class Meta:
        model=Venda
        fields=('vendedor','cliente','dataVenda')
        error_messages={
            'dataVenda':{
                'invalid':'Data de Venda Inválida',
                'required':'Informe a Data da Venda'
            },
            'cliente':{
                'required':'Informe o Cliente',
            },
            'vendedor':{
                'required':'Informe o Vendedor',
            }
        }
        widgets={
            'dataVenda':DateInput(attrs={'class':'datepicker'}),
        }
class VendaProdutoForm(ModelForm):
    class Meta:
        model=VendaProduto
        fields=('produto','quantidade')
        error_messages={
            'produto':{
                'required':'Informe o Produto',
            },
            'quantidade':{
                'required':'Informe a Quantidade',
            }
        }

VendaFormSet=inlineformset_factory(Venda,VendaProduto,fields=('produto','quantidade'))
