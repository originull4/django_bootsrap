from django.urls import path
from account.views import *


app_name='account'
urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password/change/', PasswordChangeView.as_view(), name='password-change')
]