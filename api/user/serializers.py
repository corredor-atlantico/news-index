from rest_framework import serializers

from authentification.models import User


class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'created']


class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'created']


class UserSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class UserSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']