from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie


class MoviesView(View):
    """Список фильтерв"""
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        return render(request, "movies/movie_list.html", {"movie_list": movies})



class MovieDetaiView(View):
    """Полное описание фильма"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "movies/movie_detail.html", {'movie': movie})




