from rest_framework import serializers

from core.models import Subscription


class SubscriptionSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['type', 'start_date', 'end_date']


class SubscriptionSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['type', 'start_date', 'end_date']


class SubscriptionSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['type', 'start_date', 'end_date']


class SubscriptionSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['type', 'start_date', 'end_date']
