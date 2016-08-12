from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Unidade(models.Model):
    descricao=models.CharField("Descrição",max_length=100)
    sigla=models.CharField("Sigla",max_length=5)
    def __str__(self):
        return "{0:s}-{1:s}".format(self.descricao,self.sigla)
    class Meta:
        permissions=(('view_unidade','Can see unidade'),)

class Cargo(models.Model):
    descricao=models.CharField("Descrição",max_length=150)
    def __str__(self):
        return self.descricao
    class Meta:
        permissions=(('view_cargo','Can see cargo'),)

class Pessoa(models.Model):
    nome=models.CharField("Nome",max_length=255)
    email=models.EmailField("E-Mail",max_length=200)
    telefone=models.CharField("Telefone",max_length=20)

    def __str__(self):
        return self.nome

class Cliente(Pessoa):
    endereco=models.CharField("Endereço",max_length=255)

    class Meta:
        permissions=(('view_cliente','Can see cliente'),)

class Funcionario(Pessoa):
    matricula=models.CharField("Matrícula",max_length=10,unique=True)
    cargo=models.ForeignKey(Cargo,on_delete=models.PROTECT,verbose_name="Cargo")

    class Meta:
        permissions=(('view_funcionario','Can see funcionario'),)

class Produto(models.Model):
    descricao=models.CharField("Descrição",max_length=255)
    valorUnitario=models.DecimalField("Valor Unitário",max_digits=10,decimal_places=2)
    unidade=models.ForeignKey(Unidade,on_delete=models.PROTECT,verbose_name="Unidade")

    def __str__(self):
        return self.descricao

    class Meta:
        permissions=(('view_produto','Can see produto'),)

class Venda(models.Model):
    dataVenda=models.DateField("Data da Venda")
    vendedor=models.ForeignKey(Funcionario,on_delete=models.PROTECT,verbose_name="Funcionário")
    cliente=models.ForeignKey(Cliente,on_delete=models.PROTECT,verbose_name="Cliente")
    produtos=models.ManyToManyField(Produto,through="VendaProduto")

    class Meta:
        permissions=(('view_venda','Can see venda'),)

    def __str__(self):
        return "{0:d}-{1:s}".format(self.id,self.dataVenda.strftime('%d/%m/%Y'))
    @property
    def valorTotal(self):
        lista=VendaProduto.objects.filter(venda=self) # Filtra os itens vinculados a esta venda
        #total=0
        #for item in lista: # Percorre a lista de itens, calculando o valor unitário
        #    total=total + item.produto.valorUnitario * item.quantidade
        #return total

        resultado=lista.aggregate(total=models.Sum(models.F('produto__valorUnitario')*models.F('quantidade'),output_field=models.FloatField()))
        return resultado['total']

class VendaProduto(models.Model):
    venda=models.ForeignKey(Venda,on_delete=models.CASCADE)
    produto=models.ForeignKey(Produto,on_delete=models.PROTECT)
    quantidade=models.IntegerField("Quantidade",validators=[MinValueValidator(1,message='O valor deve ser maior do que 0')])
    @property
    def subtotal(self):
        return self.produto.valorUnitario*self.quantidade

