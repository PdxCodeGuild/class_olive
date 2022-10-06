from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponseRedirect
from .models import ShorterUrlModel
import random
import string

def home_view(request):
    shorter_url_models = ShorterUrlModel.objects.all()
    context = {
        'shorter_url_models': shorter_url_models
    }
    return render(request, 'url_shorter_app/home.html', context)

def url_shortener(request):
    char_storage = string.ascii_letters + string.digits
    random_chars = random.choices(char_storage, k=6)
    random_chars = ''.join(random_chars)

    given_url = request.POST['user_url']
    given_url_split_list = given_url.split('.')

    shorter_url = given_url_split_list[0] + '/' + random_chars

    new_url_model = ShorterUrlModel(given_url=given_url, shorter_url=shorter_url)
    new_url_model.save()
    return HttpResponseRedirect(reverse('url_shorter_app:home_view'))

def url_link(request, id):
    url_link = get_object_or_404(ShorterUrlModel, id=id)
    return HttpResponseRedirect(url_link.given_url)

