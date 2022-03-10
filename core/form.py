# Create user interface to register/Login
#  users with fields [username,age,firstname,surname,hiv_status,phone_number,email,password]


# Create your models here.
from django import forms
from .models import Register,Login


class RegisterForm(forms.Form):
    HIV_STATUS = (
        ('positive', 'positive'),
        ('negative', 'negative'),
        ('unknown', 'unknown'),
    )
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }))
    age  = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Age'
        }))
    FirstName = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'First Name'
        }))
    SurName = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Sur Name'
        }))
    Hiv_status = forms.ChoiceField(choices=HIV_STATUS,widget=forms.Select(attrs={
        'class':'form-control',
        }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Phone Number'
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
        }))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
}))






