
from django import forms
from models import simulacao


class fazersimulacao(forms.ModelForm):
    class Meta:    
        model = simulacao
        fields = ('id_usuario', 'nome')
