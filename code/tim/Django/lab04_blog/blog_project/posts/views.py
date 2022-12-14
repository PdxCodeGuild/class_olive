from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog_Post
from django.contrib.auth.models import User

# class HomeListView(ListView):
#     print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#     def x(self, request):
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' + request.user)
#     model = Blog_Post
#     template_name = 'home.html'

def home(request):
    if request.user.is_authenticated:  
        all_objects = Blog_Post.objects.all()
        context = {'object_list' : all_objects}
        return render(request, 'home.html', context)
    else:
        all_objects = Blog_Post.objects.all().filter(public=True)
        context = {'object_list' : all_objects}
        return render(request, 'home.html', context)

class PostDetailView(DetailView):
    model = Blog_Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog_Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'public']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog_Post
    template_name: str = 'post_edit.html'
    fields = ['title', 'body', 'public']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog_Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author