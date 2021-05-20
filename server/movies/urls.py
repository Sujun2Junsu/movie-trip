from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('now-playing-movies/', views.now_playing_movies),
]