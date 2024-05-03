from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django_recaptcha.fields import ReCaptchaField


class RegistrationForm(UserCreationForm):
    status_choices = (
        ('user', '-'),
        ('teacher', 'Учитель'),
        ('student', 'Ученик')
    )
    captcha = ReCaptchaField()
    status = forms.ChoiceField(choices=status_choices)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'captcha']


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()