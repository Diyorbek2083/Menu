from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOnly
from django.contrib.auth.models import User
from .serializers import *
from app.models import *




class UserView(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = UserModels.objects.all()
    serializer_class = UserSerializer

class RoomViews(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = RoomModels.objects.all()
    serializer_class = RoomsSerializers

class TableView(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = TableModels.objects.all()
    serializer_class = TableSerializer
class FoodcategoryView(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = FoodCategoryaModels.objects.all()
    serializer_class = FoodCategorySerializer

class FoodView(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = FoodModels.objects.all()
    serializer_class = FoodSerializer
class CommentView(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

class ReplayCommentModelsView(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = ReplayCommentModels.objects.all()
    serializer_class = ReplayCommentSerializer

class LikeMolelsView(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = LikeMolels.objects.all()
    serializer_class = LikeSerializer


class WaiterModelsView(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = WaiterModels.objects.all()
    serializer_class = WaiterSerializer

class UserModelsView(ModelViewSet): 
    permission_classes = [IsAdminOnly]
    queryset = UserModels.objects.all()
    serializer_class = UserSerializer

class KarzinkaModelsView(ModelViewSet):
    permission_classes = [IsAdminOnly]
    queryset = KarzinkaModels.objects.all()
    serializer_class = KarzinkaSerializer

class DoimiyKarzinkaModelsView(ModelViewSet): 
    
    permission_classes = [IsAdminOnly]
    queryset = DoimiyKarzinkaModels.objects.all()
    serializer_class = DoimiyKarzinkaSerializer


    