from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.models import CustomUser
# from django.views.generic.edit import DetailView

from api.serializers import UserSerializer
from api.permissions import IsAuthorOrReadOnly
from .forms import CustomUserCreationForm, CustomUserChangeForm

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
    

# class UserProfile(DetailView):
#     model = CustomUser
#     template_name = 'user_profile.html'
#     context_object_name = 'user_profile'

