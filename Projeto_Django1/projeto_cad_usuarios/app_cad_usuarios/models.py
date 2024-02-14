from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    celular = models.TextField()
    email = models.EmailField()
    enviou_declaracao = models.CharField(max_length=5)
    alteracao_cadastral = models.CharField(max_length=5)
    conjuge = models.CharField(max_length=5)
    dependentes = models.IntegerField()
    conta_banco = models.IntegerField()
    empregado = models.CharField(max_length=5, null=True)
    mei = models.CharField(max_length=3, null=True)
    autonomo = models.CharField(max_length=5, null=True)
    aluguel = models.CharField(max_length=5, null=True)
    rural = models.CharField(max_length=5, null=True)
    pensionista = models.CharField(max_length=5, null=True)
    previdencia = models.CharField(max_length=5, null=True)
    dividendos = models.CharField(max_length=5, null=True)
    prolabore = models.CharField(max_length=5, null=True)
    exterior = models.CharField(max_length=5, null=True)
    rra = models.CharField(max_length=5, null=True)
    outras = models.CharField(max_length=5, null=True)
    despesasmedicas = models.CharField(max_length=5, null=True)
    instrucao = models.CharField(max_length=5, null=True)
    pa = models.CharField(max_length=5, null=True)
    pc = models.CharField(max_length=5, null=True)
    doacoes = models.CharField(max_length=5, null=True)
    outrasdespesas = models.CharField(max_length=5, null=True)
    imovel = models.CharField(max_length=5, null=True)
    veiculo = models.CharField(max_length=5, null=True)
    aplicacaofinan = models.CharField(max_length=5, null=True)
    acoes = models.CharField(max_length=5, null=True)
    criptoativos = models.CharField(max_length=5, null=True)
    participacaosoci = models.CharField(max_length=5, null=True)
    ouro = models.CharField(max_length=5, null=True)
    outrosbens = models.CharField(max_length=5, null=True)
    dividas = models.CharField(max_length=5)































