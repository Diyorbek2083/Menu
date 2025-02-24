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
        model = FoodsModels
        fields = '__all__'

###adasda

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategoryaModels
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodsModels
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'

class ReplayCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplayCommentModels
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeMolels
        fields = '__all__'

class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaiterModels
        fields = '__all__'

class KarzinkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = KarzinkaModels
        fields = '__all__'

class DoimiyKarzinkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoimiyKarzinkaModels
        fields = '__all__'







