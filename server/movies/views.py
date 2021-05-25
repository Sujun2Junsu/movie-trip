from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status

import requests
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .models import Movie, Review
# from django.contrib.auth import get_user_model
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, CommentListSerializer

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


@api_view(['GET'])
def movie_detail_by_pk(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    
  
### review

@api_view(['GET', 'POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def review_list(request, movie_pk):
  if request.method == 'GET':
    reviews = Review.objects.all().filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
  else:
    serializer = ReviewListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))

      movie.save()
        
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewListSerializer(review)
    return Response(serializer.data)


# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def comment_list(request, review_pk):
#   review = get_object_or_404(Review, pk=review_pk)
#   comments = review.comment_set.all()
#   serializer = CommentListSerializer(comments, many=True)
#   return Response(serializer.data)


# @api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def create_comment(request, review_pk):
#   review = get_object_or_404(Review, pk=review_pk)
#   serializer = CommentListSerializer(data=request.data)
#   if serializer.is_valid(raise_exception=True):
#     serializer.save(user=request.user, review=review)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['PUT', 'DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def review_update_delete(request, review_pk):
#   review = get_object_or_404(Review, pk=review_pk)
#   if not request.user.reviews.filter(pk=review_pk).exists():
#     return Response({'message': '권한이 없습니다.'})

#   if request.method == 'PUT':
#     serializer = ReviewListSerializer(review, data=request.data)
    
#     if serializer.is_valid(raise_exception=True):
#       movie = get_object_or_404(Movie, pk=request.data.get('movie'))
#       movie.save()
#       serializer.save(user=request.user)
#       return Response(serializer.data)

#   else:
#     review = get_object_or_404(Review, pk=review_pk)
#     movie = get_object_or_404(Movie, pk=review.movie_id)
#     movie.save()
#     review.delete()
#     return Response({ 'id': review_pk })


# @api_view(['DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def comment_delete(request, review_pk, comment_pk):
#   review = get_object_or_404(Review, pk=review_pk)
#   comment = review.comment_set.get(pk=comment_pk)
#   if not request.user.comments.filter(pk=comment_pk).exists():
#     return Response({'message': '권한이 없습니다.'})

#   else:
#     comment.delete()
#     return Response({ 'id': comment_pk })





# @api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def movie_like(request, my_pk, movie_title):
#   movie = get_object_or_404(Movie, title=movie_title)
#   me = get_object_or_404(get_user_model(), pk=my_pk)
#   if me.like_movies.filter(pk=movie.pk).exists():
#       me.like_movies.remove(movie.pk)
#       liking = False
      
#   else:
#       me.like_movies.add(movie.pk)
#       liking = True
  
#   return Response(liking)


# @api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def my_movie_like(request, my_pk):
#   me = get_object_or_404(get_user_model(), pk=my_pk)
#   data = []
#   movies = request.data
#   for movie_pk in movies:
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = MovieSerializer(movie)
#     data.append(serializer.data)
  
#   return Response(data)


# @api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def like_movie_users(request, my_pk):
#   # print(request.data)
#   users = []
#   movies = request.data.get('movies')
#   # print(movies)
#   for movie in movies:
#     movie = get_object_or_404(Movie, pk=movie)
#     serializer = MovieSerializer(movie)
#     # print(serializer.data)
#     for user in serializer.data.get('like_users'):
#       if user not in users:
#         users.append(user)

#   return Response(users)
