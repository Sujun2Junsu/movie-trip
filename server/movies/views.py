from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response

import requests
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_title):
    movie = get_object_or_404(Movie, title=movie_title)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

	
