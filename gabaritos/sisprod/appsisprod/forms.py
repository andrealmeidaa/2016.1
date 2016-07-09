from django.forms import ModelForm
from appsisprod.models import *

class ProcessoForm(ModelForm):
    class Meta:
        model=Processo
        fields=['descricao','dataInicio','dataTermino','prestadores','etapa']
class EtapaForm(ModelForm):
    class Meta:
        model=Etapa
        fields=['descricao','materiasprimas']