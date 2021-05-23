from django.db import models
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')