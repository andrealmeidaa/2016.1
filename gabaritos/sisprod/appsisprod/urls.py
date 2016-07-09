from django.conf.urls import url,include
from appsisprod.views import *
urlpatterns = [
    url(r'^$', home,name='home'),
    url(r'materiaprima/$',exibirMateriaPrima,name='materiaprima'),
    url(r'^prestadores/$',exibirPrestadores,name='prestador'),
    url(r'^processos/$',exibirProcesso,name='processo'),
]
