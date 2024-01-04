from django import forms
from . models import Userprofile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['username', 'email', 'password', 'phone_number']
        widgets = {
            'password':forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 200,widget = forms.TextInput(attrs = {'placeholder':'Enter username'}))
    password = forms.CharField(max_length=200,widget = forms.PasswordInput(attrs = {'placeholder': 'Enter password'}))