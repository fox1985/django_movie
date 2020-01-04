from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie
from  .forms import ReviewsForm


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


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewsForm(request.POST)
        movie = Movie.objects.get(id=pk)#привязка к фильму
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


