from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserForm

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