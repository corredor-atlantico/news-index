from rest_framework.decorators import action
from rest_framework.response import Response

from api.user import serializers
from rest_framework import viewsets

from authentification.models import User


class UserViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.UserSerializerList
        if self.action == "retrieve":
            return serializers.UserSerializerDetail
        if self.action == "create":
            return serializers.UserSerializerCreate
        if self.action == 'update':
            return serializers.UserSerializerUpdate
        if self.action == 'turnoff_service':
            return serializers.UserSerializerDisable
        if self.action == 'turnon_service':
            return serializers.UserSerializerActive
        return serializers.UserSerializerDetail

    @action(detail=True, methods=['post'])
    def turnoff_service(self, request, pk=None):
        serializer = self.get_serializer_class()
        qs = self.get_queryset().get(id=pk)
        disabled = serializer().deactivate_subscription(qs)
        return Response(serializer(disabled).data)

    @action(detail=True, methods=['post'])
    def turnon_service(self, request, pk=None):
        serializer = self.get_serializer_class()
        qs = self.get_queryset().get(id=pk)
        active = serializer().activate_subscription(qs)
        return Response(serializer(active).data)
