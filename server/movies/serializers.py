from rest_framework import serializers
from .models import Movie, Comment, Review


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'movie_id', 'title', 'overview', 'poster_path')


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_movies', 'like_users',)


class ReviewSerializer(serializers.ModelSerializer):

  class Meta:
    model = Review
    fields = '__all__'
    read_only_fields = ('user',)


class CommentListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ('user',)
