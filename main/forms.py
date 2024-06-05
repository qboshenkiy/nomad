from django import forms

class PhoneForm(forms.Form):
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}))
