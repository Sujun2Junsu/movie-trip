from django.urls import path
from . import views
from . import tmdb

app_name="movies"

urlpatterns = [
    path('create-movies/', tmdb.create_movies),
    path('movie-list/', views.movie_list),
    path('movie/<str:movie_title>/', views.movie_detail),
    path('movie-detail/<int:movie_pk>/', views.movie_detail_by_pk),
    path('movie-detail/<int:movie_pk>/review-list/', views.review_list),
    path('review-detail/<int:review_pk>/', views.review_detail),
    path('review/<int:review_pk>/', views.review_update_delete),
    path('review/<int:review_pk>/comment-list/', views.comment_list),
    path('review_comment/<int:comment_pk>/', views.comment_delete),
]



# urlpatterns = [
    # path('review-same-user/<int:review_pk>/', views.review_same_user),


#     path('<int:review_pk>/review_comment/', views.create_review_comment),
#     

#     path('<int:my_pk>/<movie_title>/like/', views.movie_like),
#     path('<int:my_pk>/like/', views.my_movie_like),
#     path('<int:my_pk>/like/users/', views.like_movie_users),
# ]
