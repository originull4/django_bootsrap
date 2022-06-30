from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect
from django.utils.html import format_html, mark_safe


class LoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            current_page = request.get_full_path()
            login_url = reverse('account:login')
            messages.info(request, 'You shoud login to see this page.')
            return redirect(f'{login_url}?next={current_page}')
            

class LogoutRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            current_page = request.get_full_path()
            logout_url = reverse('account:logout')
            logout_link = f'<a href="{logout_url}?next={current_page}" class="alert-link">logout</a>'
            msg = f'You are already logged in, for access to this page first {logout_link}'
            messages.info(request, format_html(msg))
            return redirect('main:home')
        else: return super().dispatch(request, *args, **kwargs)


class SuperUserOnlyMixin:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied()