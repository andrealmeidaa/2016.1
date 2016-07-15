from django.conf.urls import patterns,include,url
from appvendas.views import *
urlpatterns=[
    url(r'^$',home,name='home'),
    url(r'^produtos/$',listarprodutos,name='produtos'),
    url(r'^produtos/exibir/(\d+)$',exibirproduto,name='exibirproduto'),
    url(r'^unidade/list$', unidade_list, name='unidade_list'),
    url(r'^unidade/detail/(\d+)$', unidade_detail, name='unidade_detail'),
    url(r'^unidade/new/$',unidade_new,name='unidade_new'),
    url(r'^unidade/update/(?P<pk>\d+)',unidade_update,name='unidade_update'),
    url(r'^unidade/delete/(?P<pk>\d+)',unidade_delete,name='unidade_delete'),
    url(r'^vendas/$',listarvendas,name='vendas'),
    url(r'^clientes/$',listarclientes,name='clientes'),
    url(r'^clientes/exibir/(\d+)$',exibircliente,name='exibircliente'),
    url(r'^cargos/$',listarcargos,name='cargos'),
    url(r'^funcionarios/$',listarfuncionrios,name='funcionarios'),
    url(r'^funcionarios/exibir/(\d+)',exibirfuncionario,name='exibirfuncionario')

]