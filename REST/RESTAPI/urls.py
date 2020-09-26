from django.contrib import admin
from django.urls import path
from .views import Sample, RegisterUser, CustomCreateUser
from rest_framework_jwt.views import obtain_jwt_token

app_name = "REST"
urlpatterns = [
    path('1/', Sample.as_view()),
    path('CreateUser/', RegisterUser.as_view()),
    path('CustomCreate/', CustomCreateUser.as_view()),
    path('api-token-auth/', obtain_jwt_token),
]
