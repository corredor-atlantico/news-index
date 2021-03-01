from rest_framework import serializers

from core.models import Subscription, SubscriptionType


# MASTER SERIALIZERS
# ---------------------------
class SubscriptionTypeSerializerList(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = ['description', 'price', 'active']


class SubscriptionTypeSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = ['description', 'price', 'active']


# ---------------------------


# Model Subscription Serializers
# ---------------------------

class SubscriptionSerializerList(serializers.ModelSerializer):
    type = SubscriptionTypeSerializerDetail()

    class Meta:
        model = Subscription
        fields = ['type', 'start_date', 'end_date']


class SubscriptionSerializerDetail(serializers.ModelSerializer):
    type = SubscriptionTypeSerializerDetail()

    class Meta:
        model = Subscription
        fields = ['type', 'start_date', 'end_date', 'active']


class SubscriptionSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['type', 'start_date', 'end_date']


class SubscriptionSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['type', 'start_date', 'end_date']

# -------------------------
