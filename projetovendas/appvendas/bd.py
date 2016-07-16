
from appvendas.models import *

# Criando Unidades de Medidas

un01=Unidade(descricao='Unidade',sigla='UN')
un02=Unidade(descricao='Litro',sigla='LT')
un03=Unidade(descricao='Kilograma',sigla='KG')

un01.save() # Salva o registro no banco de dados
un02.save()

#Criando produtos

produto01=Produto(descricao='Refrigerante 2 Litros',valorUnitario=5.49,unidade=un01)
produto02=Produto(descricao='Salgado Variado',valorUnitario=2.50,unidade=un01)
produto03=Produto(descricao='Água Mineral',valorUnitario=1.50,unidade=un02)
produto01.save()
produto02.save()
produto03.save()

#Criando Clientes

cliente01=Cliente(nome='Maria Joaquina',telefone='8990-0999',endereco='Av. Lima e Silva',email='maria@mail.com.br')
cliente02=Cliente(nome='João Roberto Lima',telefone='9009-8978',endereco='Rua Florêncio Nunes',email='roberto@gmail.com')
cliente01.save()
cliente02.save()

#Criando Cargos
cargo01=Cargo(descricao='CEO')
cargo02=Cargo(descricao='Vendedor')
cargo01.save()
cargo02.save()

#Criando funcionários

func01=Funcionario(nome='João Maria da Silva',telefone='8999-0988',email='joao@mail.com',matricula='12899',cargo=cargo02)
func02=Funcionario(nome='Maria Antonieta',telefone='8788-0990',email='maria.antonieta@yahoo.com.br',matricula='90888',cargo=cargo01)

func01.save()
func02.save()

#Cadastrando o registro de uma venda

venda=Venda(cliente=cliente01,vendedor=func01,dataVenda='2016-05-27')
venda.save()
item01=VendaProduto(venda=venda,produto=produto01,quantidade=2)
item01.save()
item02=VendaProduto(venda=venda,produto=produto02,quantidade=4)
item02.save()

print(venda.valorTotal())

