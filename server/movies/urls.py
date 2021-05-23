from django.urls import path
from . import views
from . import tmdb

app_name="movies"

urlpatterns = [
    path('create-movies/', tmdb.create_movies),
    path('movies/', views.movie_list, name='movie_list'),
]