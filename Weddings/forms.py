from django import forms

class AddGuestForm(forms.Form):
    name = forms.CharField(max_length=200, error_messages={'required': '*',})
    surname = forms.CharField(max_length=200, error_messages={'required': '*',})
    email = forms.CharField(max_length=200)