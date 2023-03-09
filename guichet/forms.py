from django import forms
from .models import Etudiant



class LoginForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['cne','cin']