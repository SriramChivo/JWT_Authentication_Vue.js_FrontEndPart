from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from .serializers import UserSerailizer
from django.contrib.auth import get_user_model
import json
# Create your views here.

getmyuser = get_user_model()


class Sample(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response("Sample")


class RegisterUser(CreateAPIView):
    permission_classes=[AllowAny]
    queryset = getmyuser.objects.all()
    serializer_class = UserSerailizer


class CustomCreateUser(APIView):
    def post(self, request, *args, **kwargs):
        getData = (request.data)
        print(getData)
        userform = getmyuser.objects.create_user(
            username=getData["username"],
            email=getData["email"],
            first_name=getData["first_name"],
            last_name=getData["last_name"],
        )
        userform.set_password(getData["password"])
        userform.save()
        return Response("Done")
