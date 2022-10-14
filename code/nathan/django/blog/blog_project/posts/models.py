from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=300)
    author = models.ForeignKey('auth.User',related_name="authored_posts",on_delete=models.CASCADE)
    public =models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("posts:detail", args=(self.pk,))
        return reverse('posts:index')