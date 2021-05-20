from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie

# Create your views here.
@api_view(['GET'])
def now_playing_movies(request):
    if request.method == 'GET':
        pass
       