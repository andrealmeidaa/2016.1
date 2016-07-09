from appsisprod.models import *

processos=Processo.objects.all()

for processo in processos:
    print(processo.custoTotal)