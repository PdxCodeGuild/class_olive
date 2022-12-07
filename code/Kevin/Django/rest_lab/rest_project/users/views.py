from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


from api.serializers import UserSerializer
from . forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class CurrentUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])

