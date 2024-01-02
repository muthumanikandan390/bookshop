from django import forms
from . models import Userprofile

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['username', 'email', 'password', 'phone_number']
        widgets = {
            'password':forms.PasswordInput(),
        }