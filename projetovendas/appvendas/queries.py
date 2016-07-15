
from appvendas.models import *

#Exibe todas as Unidades, chamando o método str
print (Unidade.objects.all())

for unidade in Unidade.objects.all():
    print("Descrição: {0:s} - Sigla: {1:s}".format(unidade.descricao,unidade.sigla))

#Retorna todas as Unidades cuja a sigla seja UN

unidades=Unidade.objects.filter(sigla='UN') #Retorna uma lista de Unidades
print(unidades)

#Consulta todas as unidade cuja a sigla seja lT


unidades=Unidade.objects.filter(sigla__iexact='lT') #Retorna uma lista de Unidades
print(unidades)

#Consultando todos os funcionários que tem o nome Maria

funcionarios=Funcionario.objects.filter(nome__icontains='maria')
print(funcionarios)

#Selecionar todos os produto que custam mais de 2 reais

produtos=Produto.objects.filter(valorUnitario__gte=2)
print(produtos)

#Consultas as vendas realizadas no mês de maio

vendas=Venda.objects.filter(dataVenda__month=5)
print(vendas)

#Consultar todos os vendedores que tenham o nome Maria

funcionarios=Funcionario.objects.filter(cargo__descricao__icontains='vendedor',nome__icontains='maria')
print(funcionarios)

clientes=Cliente.objects.all().order_by('nome')
print(clientes)


cliente=Cliente.objects.get(id=1)
funcionario=Funcionario.objects.get(id=3)

produto01=Produto.objects.get(id=1)
produto02=Produto.objects.get(id=2)

#venda=Venda(cliente=cliente,vendedor=funcionario,dataVenda='2016-04-20')
#venda.save()
#item01=VendaProduto(produto=produto01,venda=venda,quantidade=3)
#item01.save()
#item02=VendaProduto(produto=produto02,venda=venda,quantidade=4)
#item02.save()

#Listando todas as vendas cadastradas

vendas=Venda.objects.all().order_by('dataVenda')

for venda in vendas:
    print("Venda: {0:d} - Vendedor : {1:s} - Cliente : {2:s} - "
          "Data: {3:s} - Total: {4:.2f}".
          format(venda.id,venda.vendedor.nome,venda.cliente.nome,
                venda.dataVenda.strftime("%d/%m/%Y"),venda.calculaValorTotal()))
    #Exibe os produtos inseridos
    itensVenda=VendaProduto.objects.filter(venda=venda)
    for item in itensVenda:
        print("Produto: {0:s} - Quantidade: {1:d} - Valor Unitário: {2:.2f} -"
              " Subtotal {3:.2f}".format(item.produto.descricao,item.quantidade,item.produto.valorUnitario,
                                         item.quantidade*item.produto.valorUnitario))
    print("---------------------------------------")




