
from django import forms
from .models import Pessoa


class formularioCadastro(forms.ModelForm):
    class Meta:    
        model = Pessoa
        fields = ('nome', 'celular', 'email', 'enviou_declaracao', 'alteracao_cadastral', 'conjuge', 'dependentes', 'conta_banco', 'empregado', 'mei', 'autonomo', 'aluguel', 'rural', 'pensionista', 'previdencia', 'dividendos', 'prolabore', 'rra', 'outras', 'despesasmedicas', 'instrucao', 'pa', 'pc', 'doacoes', 'outrasdespesas', 'imovel', 'veiculo', 'aplicacaofinan', 'acoes', 'criptoativos', 'participacaosoci', 'ouro', 'outrosbens', 'dividas')
    #def __init__(self, *args, **kwargs):
        #super(formularioCadastro, self).__init__(*args, **kwargs)
        #self.fields['nome'].error_messages['required'] =''
        #self.fields['celular'].error_messages['required'] =''
