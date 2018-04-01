from .models import UserTag
from django.contrib.auth.models import User
from rest_framework import serializers

class UserTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTag
        fields = ('id', 'uid', 'user', 'timestamp')
