from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Movie

def home_view(request):
    return HttpResponse('hello world!')

class RestListView(ListView):
    model = Movie
    template_name: str = 'home.html'

def goals_by_timeframe(request, timeframe):
    return HttpResponse(f'The timeframe is {timeframe}')