from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu correo'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tu mensaje'}),
        }
