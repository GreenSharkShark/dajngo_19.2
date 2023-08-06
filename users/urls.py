from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email-confirmation/', EmailConfirmationView.as_view(), name='email_confirmation'),
    path('verify/<int:rand_key>/', VerifyEmailView.as_view(), name='verify_email'),
    path('email-confirmed', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('email-confirmation-failed', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
]
