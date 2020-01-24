"""""
path("", views.MoviesView.as_view()),

path("<int:pk>/", views.MovieDetaiView.as_view(),  name="movie_detail")

path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail")
"""

from django.urls import path
from . import views

urlpatterns = [

    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("", views.MoviesView.as_view()), # чтобы выводила на главную траницу

]