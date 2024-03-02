
from django import forms
from .models import Pessoa


class formularioCadastro(forms.ModelForm):
    class Meta:    
        model = Pessoa
        fields = '__all__' #--todos, caso contrário deve-se destacar um a um dos campos que se pretende renderizar
        labels = {'nome': 'Nome:',
                  'celular': 'Celular:',
                    'email':'E-mail',
                    'enviou_declaracao': 'Enviou declaração em 2023?', 
                    'alteracao_cadastral': 'Teve alteração cadastral em 2023? Alteração de nome e endereço, por exemplo.',
                    'conjuge':'Possui conjuge?',
                    'dependentes':'Possui dependentes?', 
                    'conta_banco':'Quantas contas bancárias possui?', 
                    'empregado':'Empregado de empresa pública ou privada', 
                    'mei': 'MEI - Micro empreendedor individual',
                    'autonomo':'Autônomo ou Profissional Liberal', 
                    'aluguel':'Aluguel', 
                    'rural':'Atividade Rural', 
                    'pensionista':'Pensionista', 
                    'previdencia':'Previdência complementar', 
                    'dividendos':'Lucros e dividendos', 
                    'prolabore':'Pró-labore',
                    'exterior': 'Rendimentos do exterior', 
                    'rra':'Rendimentos recebidos acumuladamente', 
                    'outras':'Outras receitas', 
                    'despesasmedicas':'Despesas médicas', 
                    'instrucao': 'Despesa com instrução', 
                    'pa': 'Pensão alimentícia', 
                    'pc': 'Previdência Complementar', 
                    'doacoes':'Doações', 
                    'outrasdespesas': 'Outras despesas', 
                    'imovel': 'Imóvel', 
                    'veiculo': 'Veículo', 
                    'aplicacaofinan':'Aplicação Financeira', 
                    'acoes': 'Ações', 
                    'criptoativos':'Criptoativos', 
                    'participacaosoci': 'Participação Societária', 
                    'ouro': 'Ouro', 
                    'outrosbens':'Outros bens', 
                    'dividas': 'Dívidas acima de R$ 5.000,00'}
        widgets = {
          'nome': forms.Textarea(attrs={'rows':1, 'cols':50}),
          'celular': forms.Textarea(attrs={'rows':1, 'cols':11}),
          'email': forms.Textarea(attrs={'rows':1, 'cols':50}),
        }

