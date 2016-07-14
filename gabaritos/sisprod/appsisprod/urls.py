from django.conf.urls import url,include
from appsisprod.views import *
urlpatterns = [
    url(r'^$', home,name='home'),
    url(r'materiaprima/$',exibirMateriaPrima,name='materiaprima'),
    url(r'^prestadores/$',exibirPrestadores,name='prestador'),
    url(r'^processos/$',exibirProcesso,name='processo'),
    url(r'^cargos/$',CargoView.as_view(),name='cargos'),
    url(r'^cargos/new/$',CargoCreateView.as_view(),name="cargos-new"),
    url(r'^cargos/edit/(?P<pk>\d+)$',CargoUpdateView.as_view(),name="cargos-update"),
    url(r'^cargos/delete/(?P<pk>\d+)$',CargoDeleteView.as_view(),name="cargos-delete"),

]
