from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModels
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableModels
        fields = '__all__'

class RoomsSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomModels
        fields = '__all__'
    
class FoodCategoryaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategoryaModels
        fields = '__all__'
    
class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = FoodModels
        fields = '__all__'



