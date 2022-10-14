from django.views.generic import ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BlogPost
from django.urls import reverse_lazy

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