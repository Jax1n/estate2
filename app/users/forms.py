from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-box',
        'placeholder': 'Имя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-box',
        'placeholder': 'Пароль'
    }
    ))

    class Meta:
        labels = {""}