"""""
path("", views.MoviesView.as_view()),

path("<int:pk>/", views.MovieDetaiView.as_view(),  name="movie_detail")

path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail")
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),

    path("<slug:slug>/", views.MovieDetaiView.as_view(),  name="movie_detail")

]