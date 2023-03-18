from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'home.html'


def detailMovieView(request, id):
    movie = get_object_or_404(Movie, id=id)
    context = {'movie': movie}
    return render(request, 'detail.html', context=context)
