import os
from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')


def usuarios(request):
    #salvar os dados do formulário no banco de dados
    novo_usuario = Usuario()
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
    novo_usuario.save()
    # Exibir todos os usuários cadastrados em uma nova página.
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários.
    return render(request, 'usuarios/usuarios.html', usuarios)

    
def resultadosimulacao(request):
    # calcula o resultado da simulaçao e apresenta valor ao cliente
    checkboxinfo0 = {'':5+5}
    return render(request, 'usuarios/resultadosimulacao.html', {'':checkboxinfo0})



    
    # outrasinfo = [Number(checkboxinfo34.value), Number(checkboxinfo35.value)]

    # outrosvalores = [50, 50]

    #total2 = 0

    #html = '';
    

    #for (var n = 0; n<2; n++) {
        #total2=total2+(outrasinfo[n]*outrosvalores[n])}

    #totalgeral = total+total2 

    #return document.querySelector('#info38').innerHTML=html



