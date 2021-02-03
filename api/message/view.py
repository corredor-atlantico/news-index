from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.message import serializers
from api.message.serializers import MessageAgreeSerializer
from core.models import Message, MessageData


class MessageViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Message.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.MessageSerializerList
        if self.action == "retrieve":
            return serializers.MessageSerializerDetail
        if self.action == "create":
            return serializers.MessageSerializerCreate

    def agree(self, request, pk):
        response = MessageAgreeSerializer(self).agree_valoration()
        return Response(response, status=status.HTTP_202_ACCEPTED)
