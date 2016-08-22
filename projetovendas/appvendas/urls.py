from django.conf.urls import patterns,include,url
from django.contrib.auth.views import login,logout
from appvendas.views import *
urlpatterns=[
    url(r'^$',home,name='home'),

    url(r'^login/',login,{'template_name':'utils/login.html','redirect_field_name':'home'},name='login'),
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),


    url(r'^erro_permissao/$',erro_permissao,name='erro_permissao'),


    url(r'^produto/list$',produto_list,name='produto_list'),
    #url(r'^produto/detail/(?P<pk>\d+)$',produto_detail,name='produto_detail'),
    url(r'^produto/new/$',produto_new,name='produto_new'),
    url(r'^produto/update/(?P<pk>\d+)$',produto_update,name='produto_update'),
    url(r'^produto/delete/(?P<pk>\d+)$',produto_delete,name='produto_delete'),


    url(r'^unidade/list$', unidade_list, name='unidade_list'),
    url(r'^unidade/detail/(?P<pk>\d+)$', unidade_detail, name='unidade_detail'),
    url(r'^unidade/new/$',unidade_new,name='unidade_new'),
    url(r'^unidade/update/(?P<pk>\d+)$',unidade_update,name='unidade_update'),
    url(r'^unidade/delete/(?P<pk>\d+)$',unidade_delete,name='unidade_delete'),


    url(r'^venda/list$', venda_list, name='venda_list'),
    url(r'^venda/new/$',venda_new,name='venda_new'),
    url(r'venda/update/(?P<pk>\d+)$',venda_update,name='venda_update'),
    url(r'venda/detail/(?P<pk>\d+)$',venda_detail,name='venda_detail'),
    url(r'venda/delete/$',venda_delete,name='venda_delete'),

    url(r'^funcionario/list$', funcionario_list, name='funcionario_list'),
    url(r'^funcionario/new/$', funcionario_new, name='funcionario_new'),
    url(r'^funcionario/update/(?P<pk>\d+)$', funcionario_update, name='funcionario_update'),
    url(r'^funcionario/detail/(?P<pk>\d+)$', funcionario_detail, name='funcionario_detail'),
    url(r'^funcionario/delete/(?P<pk>\d+)$', funcionario_delete, name='funcionario_delete'),

    url(r'^cliente/list$', cliente_list, name='cliente_list'),
    url(r'^cliente/detail/(?P<pk>\d+)$', cliente_detail, name='cliente_detail'),
    url(r'^clientes/new/$', cliente_new, name='cliente_new'),
    url(r'^clientes/update/(?P<pk>\d+)$', cliente_update, name='cliente_update'),
    url(r'^clientes/delete/(?P<pk>\d+)$', cliente_delete, name='cliente_delete'),

    url(r'^cargo/list$', cargo_list, name='cargo_list'),
    url(r'^cargo/new/$', cargo_new, name='cargo_new'),
    url(r'^cargo/update/(?P<pk>\d+)$', cargo_update, name='cargo_update'),
    url(r'^cargo/delete/(?P<pk>\d+)$', cargo_delete, name='cargo_delete'),


]