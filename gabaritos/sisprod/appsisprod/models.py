from django.db import models

# Create your models here.

class Unidade(models.Model):
    descricao=models.CharField("Descrição",max_length=30)

    def __str__(self):
        return self.descricao

class MateriaPrima(models.Model):
    descricao=models.CharField("Descrição",max_length=200)
    quantidadeEstoque=models.IntegerField("Quantidade em Estoque")
    custoAquisicao=models.DecimalField("Custo",max_digits=10,decimal_places=2)
    unidade=models.ForeignKey(Unidade,on_delete=models.PROTECT,verbose_name="Unidade")

    def __str__(self):
        return self.descricao

class Cargo(models.Model):
    descricao=models.CharField("Descrição",max_length=180)
    salario=models.DecimalField("Salário",max_digits=10,decimal_places=2)
    def __str__(self):
        return self.descricao

class PrestadorServico(models.Model):
    nome=models.CharField("Nome",max_length=255)
    email=models.EmailField("E-Mail",max_length=100)
    cpf=models.CharField("CPF",max_length=11)
    telefone=models.CharField("Telefone",max_length=20)
    cargo=models.ForeignKey(Cargo,on_delete=models.PROTECT,verbose_name="Cargo")

    def __str__(self):
        return self.nome

class Processo(models.Model):
    descricao=models.CharField("Descrição",max_length=200)
    dataInicio=models.DateTimeField("Data de Início")
    dataTermino=models.DateTimeField("Data de Término",null=True,blank=True)
    prestadores=models.ManyToManyField(PrestadorServico,verbose_name="Prestadores")


    @property
    def custoTotal(self):
        custo=0
        etapas=Etapa.objects.filter(processo=self)
        for etapa in etapas:
            custo+=etapa.custoEtapa
        return custo
    def __str__(self):
        return self.descricao

class Etapa(models.Model):
    descricao=models.CharField("Descrição",max_length=200)
    processo=models.ForeignKey(Processo,on_delete=models.PROTECT,verbose_name="Processo")
    materiasprimas=models.ManyToManyField(MateriaPrima,
                                          through="EtapaMateria",
                                          verbose_name="Matérias")

    @property
    def custoEtapa(self):
        custoetapa=0
        etapamaterias=EtapaMateria.objects.filter(etapa=self)
        for etapamateria in etapamaterias:
            custoetapa+=etapamateria.subtotal
        return custoetapa

    def __str__(self):
        return self.descricao

class EtapaMateria(models.Model):
    etapa=models.ForeignKey(Etapa,verbose_name="Etapa")
    materiaPrima=models.ForeignKey(MateriaPrima,verbose_name="Matéria Prima")
    quantidade=models.IntegerField("Quantidade Utilizada")

    @property
    def subtotal(self):
        return self.quantidade*\
               float(self.materiaPrima.custoAquisicao)

    def __str__(self):
        return self.etapa.descricao + "-" + self.materiaPrima.descricao
