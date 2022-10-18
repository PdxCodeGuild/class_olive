from django.shortcuts import redirect
from django.views.generic import ListView, UpdateView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BlogPost
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Index(ListView):
    model = BlogPost
    template_name = 'index.html'

class Create_post(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'create_post.html'
    fields = ['title', 'body', 'public', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    template_name = 'post_detail.html'
    fields = ['title', 'body', 'public', 'post_image']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:index')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PicView(DetailView):
    model = BlogPost
    template_name = 'pic_view.html'

def index_register(request):

    if request.POST['password'] == request.POST['password_confirm']:
        print("PASSWORDS MATCHED")

        encrypted_password=make_password(request.POST['password'])
        user_model = User(username=request.POST['name'], password=encrypted_password)
        user_model.save()

        return redirect('posts:index')

    else:
        return redirect('posts:index') 
