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
    # path('review-same-user/<int:review_pk>/', views.review_same_user),
]



# urlpatterns = [
   
#     path('<int:movie_pk>/review_list_create/', views.review_list_create), # 리뷰 게시글 작성을 위한
#     path('review/<int:review_pk>/', views.review_update_delete),

#     path('review_comments/<int:review_pk>', views.review_comment_list),
#     path('<int:review_pk>/review_comment/', views.create_review_comment),
#     path('review_comment/<int:review_pk>/<int:review_comment_pk>/', views.review_comment_delete),

#     path('<int:my_pk>/<movie_title>/like/', views.movie_like),
#     path('<int:my_pk>/like/', views.my_movie_like),
#     path('<int:my_pk>/like/users/', views.like_movie_users),
# ]
