from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class Profile(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])