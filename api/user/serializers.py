from rest_framework import serializers

from api.subscription.serializers import SubscriptionSerializerDetail
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


class UserSerializerDisable(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', ]

    def deactivate_subscription(self, instance):
        sub = instance.subscriptions
        if sub.active:
            sub.active = False
            sub.save()
        return instance


class UserSerializerActive(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', ]

    def activate_subscription(self, instance):
        sub = instance.subscriptions
        if not sub.active:
            sub.active = True
            sub.save()
        return instance
