from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views

# app_name="accounts" 405error 발생
# app_name="accounts"

urlpatterns = [
    path('signup/', views.signup),
    # path('login/', views.login),
    path('api-token-auth/', obtain_jwt_token),
    path('user-detail/<int:user_pk>/', views.user_detail),
]