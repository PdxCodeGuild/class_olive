from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import BlogPost

class HomeListView(ListView):
    model = BlogPost
    template_name = 'home.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'
    
class Test(ListView):
    model = BlogPost
    template_name = 'home.html'



