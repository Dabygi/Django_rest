from django.urls import path

from . import views


urlpatterns = [
    path("movie/", views.MovieListView.as_view()),
    path("movie/<int:pk>/", views.MovieListView.as_view())
]
