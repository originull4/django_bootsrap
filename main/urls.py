from django.urls import path
from django.views.generic import RedirectView
from .views import *

app_name = 'main'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='main:home')),
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]