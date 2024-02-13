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
    empregado = models.CharField(max_length=5)
    mei = models.CharField(max_length=5)
    autonomo = models.CharField(max_length=5)
    aluguel = models.CharField(max_length=5)
    rural = models.CharField(max_length=5)
    pensionista = models.CharField(max_length=5)
    previdencia = models.CharField(max_length=5)
    dividendos = models.CharField(max_length=5)
    prolabore = models.CharField(max_length=5)
    exterior = models.CharField(max_length=5)
    rra = models.CharField(max_length=5)
    outras = models.CharField(max_length=5)
    despesasmedicas = models.CharField(max_length=5)
    instrucao = models.CharField(max_length=5)
    pa = models.CharField(max_length=5)
    pc = models.CharField(max_length=5)
    doacoes = models.CharField(max_length=5)
    outrasdespesas = models.CharField(max_length=5)
    imovel = models.CharField(max_length=5)
    veiculo = models.CharField(max_length=5)
    aplicacaofinan = models.CharField(max_length=5)
    acoes = models.CharField(max_length=5)
    criptoativos = models.CharField(max_length=5)
    participacaosoci = models.CharField(max_length=5)
    ouro = models.CharField(max_length=5)
    outrosbens = models.CharField(max_length=5)
    dividas = models.CharField(max_length=5)































