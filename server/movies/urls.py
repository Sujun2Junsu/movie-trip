from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    # path('auto-create-movies/', views.auto_create_movies),
    path('create-movies/', views.create_movies),
    path('movies/', views.movie_list, name='movie_list'),
]