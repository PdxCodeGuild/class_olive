from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import BlogModel

class HomeListView(ListView):
    model = BlogModel
    template_name = 'home.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogModel
    template_name = 'create_post.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('texas_app:home')

class DeletePost(DeleteView):
    model = BlogModel
    template_name = 'delete_post.html'
    success_url = reverse_lazy('texas_app:home')

class EditPost(UpdateView):
    model = BlogModel
    template_name: str = 'edit_post.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('texas_app:home')