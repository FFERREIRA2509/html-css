import os
from django.shortcuts import render
from django import templatetags
from django import template
from .models import Usuario, simulacao
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def home(request):
    return render(request,'usuarios/formfazersimulacao.html')


def usuarios(request):
    #salvar os dados do formulário no banco de dados
    novo_usuario = Usuario() #Usuario da Classe em models
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.celular = request.POST.get('celular')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.enviou_declaracao = request.POST.get('enviou_declaracao')
    novo_usuario.alteracao_cadastral = request.POST.get('alteracao_cadastral')
    novo_usuario.conjuge = request.POST.get('conjuge')
    novo_usuario.dependentes = request.POST.get('dependentes')
    novo_usuario.conta_banco = request.POST.get('conta_banco')
    novo_usuario.empregado = request.POST.get('empregado')
    novo_usuario.mei = request.POST.get("mei")
    novo_usuario.autonomo = request.POST.get('autonomo')
    novo_usuario.aluguel = request.POST.get('aluguel')
    novo_usuario.rural = request.POST.get('rural')
    novo_usuario.pensionista = request.POST.get('pensionista')
    novo_usuario.previdencia = request.POST.get('previdencia')
    novo_usuario.dividendos = request.POST.get('dividendos')
    novo_usuario.prolabore = request.POST.get('prolabore')
    novo_usuario.exterior = request.POST.get('exterior')
    novo_usuario.rra = request.POST.get('rra')
    novo_usuario.outras = request.POST.get('outras')
    novo_usuario.despesasmedicas = request.POST.get('despesasmedicas')
    novo_usuario.instrucao = request.POST.get('instrucao')
    novo_usuario.pa = request.POST.get('pa')
    novo_usuario.pc = request.POST.get('pc')
    novo_usuario.doacoes = request.POST.get('doacoes')
    novo_usuario.outrasdespesas = request.POST.get('outrasdespesas')
    novo_usuario.imovel = request.POST.get('imovel')
    novo_usuario.veiculo = request.POST.get('veiculo')
    novo_usuario.aplicacaofinan = request.POST.get('aplicacaofinan')
    novo_usuario.acoes = request.POST.get('acoes')
    novo_usuario.criptoativos = request.POST.get('criptoativos')
    novo_usuario.participacaosoci = request.POST.get('participacaosoci')
    novo_usuario.ouro = request.POST.get('ouro')
    novo_usuario.outrosbens = request.POST.get('outrosbens')
    novo_usuario.dividas = request.POST.get('dividas')
    novo_usuario.save()#salva no banco de dados
    # Exibir todos os usuários cadastrados em uma nova página.
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários.
    # calcula o resultado da simulaçao e apresenta valor ao cliente
    teste = Usuario.objects.all()
    checkboxinfo0 = {'Valor': teste}
    return render(request, 'usuarios/resultadosimulacao.html', {'Valor':teste})# esse usuarios é da pasta do templates
    #return render(request, 'usuarios/usuarios.html', usuarios)



def fazersimulacao(request): 
    return render(request, 'usuarios/formfazersimulacao.html')

#render(request, 'usuarios/formfazersimulacao.html', context=context)# esse usuarios é da pasta do templates
#salvar os dados do formulário no banco de dados
    """novo_usuario = Usuario() #Usuario da Classe em models
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.celular = request.POST.get('celular')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.enviou_declaracao = request.POST.get('enviou_declaracao')
    novo_usuario.alteracao_cadastral = request.POST.get('alteracao_cadastral')
    novo_usuario.conjuge = request.POST.get('conjuge')
    novo_usuario.dependentes = request.POST.get('dependentes')
    novo_usuario.conta_banco = request.POST.get('conta_banco')
    novo_usuario.empregado = request.POST.get('empregado')
    novo_usuario.mei = request.POST.get("mei")
    novo_usuario.autonomo = request.POST.get('autonomo')
    novo_usuario.aluguel = request.POST.get('aluguel')
    novo_usuario.rural = request.POST.get('rural')
    novo_usuario.pensionista = request.POST.get('pensionista')
    novo_usuario.previdencia = request.POST.get('previdencia')
    novo_usuario.dividendos = request.POST.get('dividendos')
    novo_usuario.prolabore = request.POST.get('prolabore')
    novo_usuario.exterior = request.POST.get('exterior')
    novo_usuario.rra = request.POST.get('rra')
    novo_usuario.outras = request.POST.get('outras')
    novo_usuario.despesasmedicas = request.POST.get('despesasmedicas')
    novo_usuario.instrucao = request.POST.get('instrucao')
    novo_usuario.pa = request.POST.get('pa')
    novo_usuario.pc = request.POST.get('pc')
    novo_usuario.doacoes = request.POST.get('doacoes')
    novo_usuario.outrasdespesas = request.POST.get('outrasdespesas')
    novo_usuario.imovel = request.POST.get('imovel')
    novo_usuario.veiculo = request.POST.get('veiculo')
    novo_usuario.aplicacaofinan = request.POST.get('aplicacaofinan')
    novo_usuario.acoes = request.POST.get('acoes')
    novo_usuario.criptoativos = request.POST.get('criptoativos')
    novo_usuario.participacaosoci = request.POST.get('participacaosoci')
    novo_usuario.ouro = request.POST.get('ouro')
    novo_usuario.outrosbens = request.POST.get('outrosbens')
    novo_usuario.dividas = request.POST.get('dividas')
    novo_usuario.save()#salva no banco de dados
    # Exibir todos os usuários cadastrados em uma nova página.
    usuarios = {
        'usuarios': simulacao.objects.all()
    }"""
    # Retornar os dados para a página de listagem de usuários.
    # calcula o resultado da simulaçao e apresenta valor ao cliente
    #form = {'form': Teste}
    

