from django import forms
from Apps.Noticias.models import *

CHOICES = (
    ('', ''),
    ('noticias', 'Noticias'),
    ('eventos', 'Eventos'),
)

class NoticiaCrearForm(forms.ModelForm):
    class Meta:
        model = NoticiasModelo

        fields=[
            'titulo', 
            'resumen', 
            'detalle',
            'fecha',
            'tipo',
            
        ]



        labels={
            'titulo':'Título',
            'resumen':'Resumen',
            'detalle':'Detalle',
            'fecha':'Fecha',
            'tipo': 'Tipo'
            
            
        }

        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'resumen':forms.TextInput(attrs={'class':'form-control'}),
            'detalle':forms.Textarea(attrs={'class':'form-control'}),
            'fecha':forms.DateInput(attrs={'class':'form-control'}),
            'tipo':forms.Select(choices=CHOICES),

            

        }


