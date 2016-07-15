from django.conf.urls import url,include
from appsisprod.views import *

'''
Padronizando o padrao de urls:
modelo-list (Lista a relação de modelos)
modelo-edit (Edita uma instância específica)
modelo-delete (Deleta um instância)
modelo-new (Adiciona um novo objeto do modelo)
'''

urlpatterns = [
    url(r'^$', home,name='home'),
    url(r'materiaprima/$',exibirMateriaPrima,name='materiaprima'),
    url(r'^prestador/$', prestador_list, name='prestador-list'),
    url(r'^prestador/new/$',prestador_new,name='prestador-new'),
    url(r'^prestador/edit/(?P<pk>\d+)$',prestador_edit,name='prestador-edit'),
    url(r'^prestador/delete/$',prestador_delete,name='prestador-delete'),
    url(r'^processos/$',exibirProcesso,name='processo'),
    url(r'^cargo/$',CargoView.as_view(),name='cargo-list'),
    url(r'^cargo/new/$',CargoCreateView.as_view(),name="cargo-new"),
    url(r'^cargo/edit/(?P<pk>\d+)$',CargoUpdateView.as_view(),name="cargo-update"),
    url(r'^cargo/delete/(?P<pk>\d+)$',CargoDeleteView.as_view(),name="cargo-delete"),


]
