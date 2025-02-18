from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOnly
from django.contrib.auth.models import User
from .serializers import *




class UserView(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

