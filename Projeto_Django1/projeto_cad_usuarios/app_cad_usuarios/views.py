import os
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django import templatetags
from django import template
from .models import Usuario
from .models import Pessoa
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import formularioCadastro
import requests



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

def formatar_numero(valor):
  if valor == '':
    return '0.00'
  valor=float(valor)
  valor="{:_.2f}".format(valor)
  valor=str(valor)
  valor=valor.replace(".", ",").replace("_", ".")
  return valor



def fazersimulacao(request):
   if request.method == 'GET':
        cadastro = Pessoa.objects.all()
        form = formularioCadastro()
        context= {
            'cadastro':cadastro,
            'form':form,
        }
        return render(request, 'usuarios/formfazersimulacao.html', context)
   elif request.method == 'POST':
       form = formularioCadastro(request.POST)
       if form.is_valid():
            form.save()
            cadastro = Pessoa.objects.all()
            for k, pessoa in enumerate(cadastro):
                if k == len(cadastro)-1:
                    if pessoa.conta_banco > 0:
                        enviou_declaracao = float(float(pessoa.enviou_declaracao) * -50)
                        alteracao_cadastral = float(float(pessoa.alteracao_cadastral) * 10)
                        conjuge = float(float(pessoa.conjuge) * 50)
                        dependentes = float(float(pessoa.dependentes) * 10)
                        conta_banco= float(pessoa.conta_banco * 10.0)
                        empregado = float(float(pessoa.empregado) * 10)
                        mei = float(float(pessoa.mei) * 50)
                        autonomo = float(float(pessoa.autonomo) * 50)
                        aluguel = float(float(pessoa.aluguel) * 50)
                        rural = float(float(pessoa.rural) * 50)
                        pensionista = float(float(pessoa.pensionista) * 10)
                        previdencia = float(float(pessoa.previdencia) * 10)
                        dividendos = float(float(pessoa.dividendos) * 50)
                        prolabore = float(float(pessoa.prolabore) * 10)
                        exterior = float(float(pessoa.exterior) * 50)
                        rra = float(float(pessoa.rra) * 10)
                        outras = float(float(pessoa.outras) * 50)
                        despesasmedicas = float(float(pessoa.despesasmedicas) * 50)
                        instrucao = float(float(pessoa.instrucao) * 10)
                        pa = float(float(pessoa.pa) * 30)
                        pc = float(float(pessoa.pc) * 10)
                        doacoes = float(float(pessoa.doacoes) * 10)
                        outrasdespesas = float(float(pessoa.outrasdespesas) * 10)
                        imovel = float(float(pessoa.imovel) * 20)
                        veiculo = float(float(pessoa.veiculo) * 10)
                        aplicacaofinan = float(float(pessoa.aplicacaofinan) * 10)
                        acoes = float(float(pessoa.acoes) * 50)
                        criptoativos = float(float(pessoa.criptoativos) * 50)
                        participacaosoci = float(float(pessoa.participacaosoci) * 10)
                        ouro = float(float(pessoa.ouro) * 10)
                        outrosbens = float(float(pessoa.outrosbens) * 10)
                        dividas = float(float(pessoa.dividas) * 10)
                        total_simulacao = enviou_declaracao + alteracao_cadastral + conjuge + dependentes + conta_banco + empregado + mei + autonomo + aluguel + rural + pensionista + previdencia + dividendos + prolabore + exterior + rra + outras + despesasmedicas + instrucao + pa + pc + doacoes + outrasdespesas + imovel + veiculo + aplicacaofinan + acoes + criptoativos + participacaosoci + ouro + outrosbens + dividas

                        if total_simulacao < 99:
                            total_simulacao = 99
                        
                        total_simulacao = formatar_numero(total_simulacao)

                        context= {
                            'total': total_simulacao
                            }
                        return render(request, 'usuarios/resultadosimulacao.html', context)
            else:
                cadastro = Pessoa.objects.all()
                context= {
                    'cadastro':cadastro,
                    'form':form,
                    }
                return render(request, 'usuarios/formfazersimulacao.html', context)
   
cadastro = Pessoa.objects.all()


print(len(cadastro))


def imposto_de_renda(request):
    return render(request, 'usuarios/imposto_de_renda.html')

def f4(request):
    return render(request, 'usuarios/f4.html')

def artigos(request):
    return render(request, 'usuarios/artigos.html')

def serviços(request):
    return render(request, 'usuarios/serviços.html')

def modelo(request):
    return render(request, 'usuarios/modelo.html')


def fale(request):
    return render(request, 'usuarios/falecomcontador.html')

