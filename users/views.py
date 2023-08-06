from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
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
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:main')
