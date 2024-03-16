from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Todo


# Own UserSerializer
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#           'id',
#           'username',
#           'email',
#           'first_name',
#           'last_name',
#         ]       


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()       #Own UserSerializer
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault()) 
    class Meta:
        model = Todo
        fields = [
          'id',
          'title', 
          'description', 
          'created_at',
          'user',
          'time_passed' 
        ]
