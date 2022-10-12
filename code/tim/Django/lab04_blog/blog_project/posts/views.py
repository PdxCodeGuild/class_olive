from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog_Post

# class HomeListView(ListView):
#     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#     def x(self, request):
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' + request.user)
#     model = Blog_Post
#     template_name = 'home.html'

def home(request):
    all_objects = Blog_Post.objects.all()
    context = {
        'object_list' : all_objects
    }
    return render(request, 'home.html', context)

class PostDetailView(DetailView):
    model = Blog_Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog_Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)