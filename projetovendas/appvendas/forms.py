from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from appvendas.models import *
class UnidadeForm(ModelForm):
   class Meta:
       model=Unidade
       fields=('descricao','sigla')
class ProdutoForm(ModelForm):
    class Meta:
        model=Produto
        fields=('descricao','unidade','valorUnitario')

class VendaForm(ModelForm):
    class Meta:
        model=Venda
class VendaProdutoForm(ModelForm):
    class Meta:
        model=VendaProduto

VendaFormSet=inlineformset_factory(Venda,VendaProduto)
