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


class ReviewListSerializer(serializers.ModelSerializer):
  # movie_title = serializers.SerializerMethodField()

#   def get_movie_title(self, obj):
#     return obj.movie.title

#   userName = serializers.SerializerMethodField()
  
#   def get_userName(self,obj):
#     return obj.user.username

  class Meta:
    model = Review
    fields = '__all__'
    read_only_fields = ('user', 'movie',)


class CommentListSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  
#   def get_userName(self,obj):
#     return obj.user.username

  class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ('user', 'review',)
