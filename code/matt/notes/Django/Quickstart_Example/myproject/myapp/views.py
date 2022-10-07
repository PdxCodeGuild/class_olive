from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import BlogPost

def myview(request):
    my_dataset = BlogPost.objects.all()
    context = {
        'blog_posts': my_dataset
    }

    return render(request, 'myapp/home.html', context)

def new_post(request):
    # print('!!!!!!!', request.POST, '!!!!!!!!!!!')
    # print(request.POST['title'])
    # print(request.POST['text'])

    title_field = request.POST['title']
    text_field = request.POST['text']


    mymodel = BlogPost(title=title_field, text=text_field)
    mymodel.save()
    return HttpResponseRedirect(reverse('myapp:myview'))


def edit_post(request, id):
    print(request)
    post = get_object_or_404(BlogPost, id=id)

    post.active = not post.active
    post.save()
    return redirect('myapp:myview')