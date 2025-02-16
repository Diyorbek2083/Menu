from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny 
from django.contrib.auth.models import User
from .serializers import ModelSelializer
class PostApi(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = ModelSelializer