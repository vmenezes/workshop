from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Movie
from .forms import MovieForm


class IndexView(View):
    def get(self, request):
        movies = Movie.objects.all()
        context = {"movies": movies}
        return render(request, "movies/index.html", context)


class AddMovieView(View):
    def get(self, request):
        movie_form = MovieForm()
        context = {"form": movie_form.as_p()}
        return render(request, "movies/add.html", context)
    
    def post(self, request):
        movie_form = MovieForm(request.POST)
        new_movie = movie_form.save()
        return redirect("index")