from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Movie

def home_view(request):
    all_movies = Movie.objects.all()
    context = {
        'all_movies' : all_movies
    }
    return render(request, 'movie_app/home.html', context)


def new_movie(request):
    # print('!!!!!!!!!!!!!!!!!!!!!!!!', request.POST)

    title = request.POST['title']
    director = request.POST['director']
    release_date = request.POST['release_date']
    genre = request.POST['genre']
    in_theatres = request.POST['in_theatres']

    if in_theatres == 'on':
        in_theatres = True
    else:
        in_theatres = False

    movie_model = Movie(title=title, director=director, release_date=release_date, genre=genre, in_theatres=in_theatres)
    movie_model.save()
    return redirect('movie_app:home')

def toggle_in_theatres(request, id):
    # print("Movie ID", id)
    movie_obj = get_object_or_404(Movie, id=id)
    # print(movie_obj.in_theatres)

    movie_obj.in_theatres = not movie_obj.in_theatres
    movie_obj.save()

    return redirect('movie_app:home')


def delete_movie(request, id):
    movie_obj = get_object_or_404(Movie, id=id)
    movie_obj.delete()

    return redirect('movie_app:home')