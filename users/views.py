from django.http import HttpResponseRedirect
from users.services import *
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView, FormView

from users.forms import UserRegisterForm, UserProfileForm, UserResetPasswordForm
from users.models import User


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('catalog:main')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    """
    Класс для регистрации пользователя на сайте.
    """
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:email_confirmation')

    def form_valid(self, form):
        made_rand_key_for_verify_and_send_mail(self, form)
        return super().form_valid(form)


class VerifyEmailView(View):
    @staticmethod
    def get(rand_key):
        try:
            user = User.objects.get(rand_key=rand_key)
            user.is_active = True
            user.save()
            return HttpResponseRedirect(reverse('users:email_confirmed'))
        except User.DoesNotExist:
            return HttpResponseRedirect(reverse('users:email_confirmation_failed'))


class ResetPasswordView(FormView):
    """
    Класс для сброса пароля на автоматически сгенерированный
    """
    model = User
    template_name = 'users/reset_password.html'
    form_class = UserResetPasswordForm
    success_url = reverse_lazy('users:reset_password_done')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        reset_password_and_send_mail(username)
        return super().form_valid(form)


class EmailConfirmationView(TemplateView):
    template_name = 'users/email_confirmation_sent.html'


class EmailConfirmedView(TemplateView):
    template_name = 'users/email_confirmed.html'


class EmailConfirmationFailedView(TemplateView):
    template_name = 'users/email_confirmation_failed.html'
