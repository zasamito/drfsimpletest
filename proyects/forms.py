from django import forms
from .models import Proyect

class ProyectForm(forms.ModelForm):
    class Meta:
        model = Proyect
        fields = ['title', 'description', 'technology']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Titulo Proyecto'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Descripcion',
                'rows': 4
            }),
            'technology': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Tecnologia (e.g., Django, React)',
            }),
        }