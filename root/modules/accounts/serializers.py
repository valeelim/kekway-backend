from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

User = get_user_model()

class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('codename',)


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'username', 'role', 'password', )


class UserSerializer(UserSerializer):
    user_permissions = UserPermissionSerializer(many=True)

    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'username', 'bio', 'role', 'user_permissions', 'profile_photo', 'background_photo',)


class UserOnlyIdAndNameAndUsername(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'name', 'username')



