from django.urls import path
from . import views
from . import tmdb

app_name="movies"

urlpatterns = [
    path('create-movies/', tmdb.create_movies),
    path('movie-list/', views.movie_list, name='movie_list'),
    path('movie/<str:movie_title>/', views.movie_detail, name='movie_detail'),
]