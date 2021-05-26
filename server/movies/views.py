from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status

import requests
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .models import Movie, Review, Comment
# from django.contrib.auth import get_user_model
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer, CommentListSerializer

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
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list(request, movie_pk):
  if request.method == 'GET':
    reviews = Review.objects.all().filter(movie_id=movie_pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
  else:
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))
      movie.save()
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)

  if not request.user.user_reviews.filter(pk=review_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
    serializer = ReviewSerializer(review, data=request.data)
    
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))
      movie.save()
      serializer.save(user=request.user)
      return Response(serializer.data)

  elif request.method == 'DELETE':
    review.delete()
    return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list(request, review_pk):
  if request.method == 'GET':
    comments = Comment.objects.all().filter(review_id=review_pk)
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)
  else:
    serializer = CommentListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      review = get_object_or_404(Review, pk=review_pk)
      review.save()
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_pk):
  comment = get_object_or_404(Comment, pk=comment_pk)
  if not request.user.user_comments.filter(pk=comment_pk).exists():
    return Response({'message': '권한이 없습니다.'})
  else:
    comment.delete()
    return Response({ 'id': comment_pk })


# @api_view(['GET'])
# # 로그인한 유저가 리뷰 작성 유저인지 확인하는 용도
# def review_same_user(request, review_pk):
#   if not request.user.user_reviews.filter(pk=review_pk).exists():
#     return Response({'message': '권한이 없습니다.'})
#   return Response({'message': '권한이 있습니다.'})


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
