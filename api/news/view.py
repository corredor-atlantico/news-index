from rest_framework import viewsets

from api.news import serializers
from core.models import New


class NewViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return New.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MessageSerializerList
        if self.action == "retrieve":
            return serializers.MessageSerializerDetail
        if self.action == "create":
            return serializers.MessageSerializerCreate