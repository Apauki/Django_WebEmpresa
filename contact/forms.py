from socket import fromshare
from django import forms

class ContactForm():
    name=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': "Ej: Juan Perez"}))
    email=forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder': "Ej: jperez@hotmail.com"}))
    content=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'placeholder': "Escribe tu mensaje"}))