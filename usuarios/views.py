from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
User = get_user_model()


# Create your views here.
class LoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = AuthenticationForm


class RegistrarView(SuccessMessageMixin, CreateView):
    template_name = 'auth/registrar.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('usuarios:login')
    success_message = "%(username)s se registró de manera exitosa"

    def form_valid(self, form):
        user = form.save()
        user.save()

        return super().form_valid(form)
