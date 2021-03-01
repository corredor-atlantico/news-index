from rest_framework import viewsets

from api.subscription import serializers
from core.models import Subscription


class SubscriptionViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Subscription.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.SubscriptionSerializerList
        if self.action == "retrieve":
            return serializers.SubscriptionSerializerDetail
        if self.action == 'update':
            return serializers.SubscriptionSerializerUpdate
