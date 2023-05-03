from django.core import validators
from django import forms
from .models import Contact,Comment

class ContactRegistration(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['nom','email','sujet','message']
        widgets={

        }
class CommentsRegistration(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['nom','email','commentaire']
        widgets={
            'nom':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'Commentaire':forms.TextInput(attrs={'class':'form-control','rows':'10'}),
        }
    