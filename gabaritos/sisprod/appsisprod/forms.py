from django.forms import ModelForm
from appsisprod.models import *

class PrestadorServicoForm(ModelForm): #Cria um form baseado e um modelo
    class Meta:
        model=PrestadorServico #Define o modelo vinculado ao Form
        fields=('nome','email','cpf','telefone','cargo') #Estabelece quais campos deve ser exibidos

