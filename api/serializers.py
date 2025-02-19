from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablesModels
        fields = '__all__'

class RoomsSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomModels
        fields = '__all__'

