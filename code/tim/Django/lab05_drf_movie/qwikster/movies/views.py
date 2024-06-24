from django.views.generic import ListView
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'home.html'
