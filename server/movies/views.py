from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response

import requests, pprint, json
from django.shortcuts import render, redirect, get_list_or_404
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie

def create_movies(request):

    results = []
   
    # data 받아오기
    # https://api.themoviedb.org/3/movie/now_playing?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR
    # https://api.themoviedb.org/3/movie/top_rated?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR
    # https://api.themoviedb.org/3/movie/popular?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR
    my_url = 'https://api.themoviedb.org/3/movie/popular?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR'
    response = requests.get(my_url)
    movie_dict = response.json()
    # return Response(movie_dict)

    # 필요한 정보 골라내기
    movie_list = movie_dict.get('results')
    for movie in movie_list:
        title = movie.get('original_title')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        poster_path = movie.get('poster_path')
        popularity = movie.get('popularity')

        # # DB에 저장하기, 중복제거
        # (movie, created) = Movie.objects.get_or_create(title=title, overview=overview, release_date=release_date, poster_path=poster_path, popularity=popularity)

        results.append({
            "model": "movies.movie",
            "pk": len(results) + 1,
            "fields": {
            "poster_path": "https://image.tmdb.org/t/p/w500" +  poster_path,
            "title": title,
            "overview": overview,
            "release_date": release_date,
            "popularity": popularity
        }})

    my_url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR'
    response = requests.get(my_url)
    movie_dict = response.json()
    # return Response(movie_dict)

    # 필요한 정보 골라내기
    movie_list = movie_dict.get('results')
    for movie in movie_list:
        title = movie.get('original_title')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        poster_path = movie.get('poster_path')
        popularity = movie.get('popularity')

        # # DB에 저장하기, 중복제거
        # (movie, created) = Movie.objects.get_or_create(title=title, overview=overview, release_date=release_date, poster_path=poster_path, popularity=popularity)

        results.append({
            'model': "movies.movie",
            'pk': len(results) + 1,
            "fields": {
            'poster_path': 'https://image.tmdb.org/t/p/w500' +  poster_path,
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'popularity': popularity
        }})

    my_url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR'
    response = requests.get(my_url)
    movie_dict = response.json()
    # return Response(movie_dict)

    # 필요한 정보 골라내기
    movie_list = movie_dict.get('results')
    for movie in movie_list:
        title = movie.get('original_title')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        poster_path = movie.get('poster_path')
        popularity = movie.get('popularity')

        # # DB에 저장하기, 중복제거
        # (movie, created) = Movie.objects.get_or_create(title=title, overview=overview, release_date=release_date, poster_path=poster_path, popularity=popularity)

        results.append({
            'model': "movies.movie",
            'pk': len(results) + 1,
            "fields": {
            'poster_path': 'https://image.tmdb.org/t/p/w500' +  poster_path,
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'popularity': popularity
        }})

    pprint.pprint(results)
    with open('movies2.json', "w", encoding='utf-8') as f: # movies.json은 저장될 json 파일 명입니다., json_data은 저장할 데이터입니다.
        json.dump(results, f, ensure_ascii=False)
    return None


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


	
