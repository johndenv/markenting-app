from django import forms
from .models import DataMovie

class DataMovieForm(forms.ModelForm):
    
    class Meta:
        model = DataMovie

        fields = ['text', 'context', 'public', 'number_public']
        
        labels = {
            'text': 'Texto/Análise do Vídeo',
            'context': 'Contexto do Conteúdo',
            'public': 'Perfil do Público',
            'number_public': 'Volume do Público (Número)',
        }

        help_texts = {
            'text': 'Insira a transcrição, descrição ou análise detalhada do vídeo.',
            'context': 'Ex: Culinária, Finanças, Jogos Violentos, etc.',
            'public': 'Ex: Jovens de 18-24 anos, Empreendedores, etc.',
            'number_public': 'Quantidade estimada de pessoas alcançadas ou visualizações.',
        }

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5, 
                'placeholder': 'Digite ou cole o texto aqui...'
            }),
            'context': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: Tecnologia / Gadgets'
            }),
            'public': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: Homens de 25 a 34 anos'
            }),
            'number_public': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': '0'
            }),
        }

    def clean_number_public(self):
        """
        Validação customizada para o campo 'number_public'.
        Garante que o número de público não seja negativo.
        """
        number_public = self.cleaned_data.get('number_public')
        
        if number_public is not None and number_public < 0:
            raise forms.ValidationError("O volume do público não pode ser um número negativo.")
            
        return number_public
