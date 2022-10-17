from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Post

# def home_view(request):
#     all_posts = Post.objects.all()
#     context = {
#         'posts': all_posts
#     }
    
#     return render(request, 'base.html', context)


class HomeListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name: str = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def HomeRegister(request):
    # print('!!!!!!!!!!!!!!!!!', request.POST['password2'])
    # print(request.POST['password'])
    # print(request.POST['password2'])

    if request.POST['password'] == request.POST['password2']:
        print("PASSWORDS MATCHED")

        encrypted_password=make_password(request.POST['password'])
        user_model = User(username=request.POST['name'], password=encrypted_password)
        user_model.save()

        return redirect('posts:home')

    else:
        return redirect('posts:home')