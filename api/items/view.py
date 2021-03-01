from rest_framework import viewsets, status
from rest_framework.response import Response

from api.items import serializers
from core.models import Items


class ItemViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Items.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ItemSerializerList
        if self.action == "retrieve":
            return serializers.ItemSerializerDetail
        if self.action == "create":
            return serializers.ItemSerializerCreate
        if self.action == 'update':
            return serializers.ItemSerializerUpdate
