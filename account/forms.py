from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from account.models import Account



class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = Account
        fields = ('username', 'email', 'gender', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
            visible.field.widget.attrs['placeholder'] = visible.label


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control form-control-sm'
            field.field.widget.attrs['placeholder'] = field.label


class PasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control form-control-sm'
            field.field.widget.attrs['placeholder'] = field.label