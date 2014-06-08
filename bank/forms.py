from django import forms

class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField()
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)