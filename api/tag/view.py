from rest_framework import viewsets

from api.tag import serializers
from core.models import Tag


class TagViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Tag.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.TagSerializerList
        if self.action == "retrieve":
            return serializers.TagSerializerDetail
        if self.action == "create":
            return serializers.TagSerializerCreate