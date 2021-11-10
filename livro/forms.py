from django import forms
from .models import Livros


class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()


class CategoriaLivro(forms.Form):
    nome = forms.CharField(max_length=30)
    descricao = forms.CharField(widget=forms.Textarea)
