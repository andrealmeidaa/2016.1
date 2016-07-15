from django.conf.urls import patterns,include,url
from appvendas.views import *
urlpatterns=[
    url(r'^$',home,name='home'),

    url(r'^produto/list$',produto_list,name='produto_list'),
    #url(r'^produto/detail/(?P<pk>\d+)$',produto_detail,name='produto_detail'),
    url(r'^produto/new/$',produto_new,name='produto_new'),
    url(r'^produto/update/(?P<pk>\d+)$',produto_update,name='produto_update'),
    #url(r'^produto/delete/(?P<pk>\d+)$',produto_delete,name='produto_delete'),


    url(r'^unidade/list$', unidade_list, name='unidade_list'),
    url(r'^unidade/detail/(?P<pk>\d+)$', unidade_detail, name='unidade_detail'),
    url(r'^unidade/new/$',unidade_new,name='unidade_new'),
    url(r'^unidade/update/(?P<pk>\d+)$',unidade_update,name='unidade_update'),
    url(r'^unidade/delete/(?P<pk>\d+)$',unidade_delete,name='unidade_delete'),


    url(r'^vendas/$',listarvendas,name='vendas'),
    url(r'^clientes/$',listarclientes,name='clientes'),
    url(r'^clientes/exibir/(\d+)$',exibircliente,name='exibircliente'),
    url(r'^cargos/$',listarcargos,name='cargos'),
    url(r'^funcionarios/$',listarfuncionrios,name='funcionarios'),
    url(r'^funcionarios/exibir/(\d+)',exibirfuncionario,name='exibirfuncionario')

]