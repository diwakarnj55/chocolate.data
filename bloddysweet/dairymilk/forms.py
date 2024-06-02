from django import forms
from .models import Contact
from django . forms import Textarea,Select,TextInput

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields =['name','email','phone','message']

        widgets ={
            'name':TextInput(attrs={
             "type":"text", 
             "placeholder":"Full Name",
             }),
            'phone':TextInput(attrs={
             "type":"text", 
             "placeholder":"Phone number",
             }),
            'email':TextInput(attrs={
             "type":"email", 
            "placeholder":"Email",
             }),
            'message':TextInput(attrs={
             "type":"text", 
             "class":"message-box", 
             "placeholder":"Message",
             }),
    }