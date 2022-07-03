from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.views.generic import View
from account.forms import *
from config.mixins import SuperUserOnlyMixin, LoginRequiredMixin, LogoutRequiredMixin
from django.utils.translation import gettext as _


class RegistrationView(LogoutRequiredMixin, View):

    template_name = 'account/register.html'
    form = RegistrationForm
    success_message = _('Your account has been created successfully and you are logged in.')
    error_message = _('Registration failed!!! Check your infromations and try again.')

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, self.success_message)
            return redirect('account:profile')
        messages.error(request, self.error_message)
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})


class ProfileView(LoginRequiredMixin, View):
    
    template_name = 'account/profile.html'

    def get(self, request):
        user_info = {
            'username': request.user.username,
            'email': request.user.email or '-----------',
            'first_name': request.user.first_name or '-----------',
            'last_name': request.user.last_name or '-----------',
            'date_joined': request.user.date_joined,
            'gender': request.user.gender or '-----------',
            'avatar': request.user.avatar.url,
        }
        return render(request, self.template_name, user_info)


class LoginView(LogoutRequiredMixin, View):

    template_name = 'account/login.html'
    form = LoginForm
    success_message = _('you are logged in successfully.')
    error_message = ''

    def post(self, request):
        form = self.form(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, self.success_message)
            if 'next' in request.GET: return redirect (request.GET.get('next'))
            return redirect('account:profile')
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})


class LogoutView(LoginRequiredMixin, View):

    template_name = 'account/logout.html'

    def get(self, request):
        logout(request)
        return render(request, self.template_name)


class PasswordChangeView(View):

    template_name = 'account/password_change.html'
    form = PasswordForm
    success_message = _('Your password has been changed successfully.')
    error_message = _('Password change failed!!!. Please check your information and try again.')

    def post(self, request):
        form = self.form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, self.success_message)
            return redirect('account:profile')
        messages.error(request, self.error_message)
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        self.form = self.form(user=request.user)
        return render(request, self.template_name, {'form': self.form})
