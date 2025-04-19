from django import forms
from myapp.models import Klub

class KlubForm(forms.ModelForm):

    class Meta:
        model = Klub
        fields = ('nama', 'negara', 'tahunberdiri')
        widgets = {

            "nama" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),

            "negara" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                }),
        }