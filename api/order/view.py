from django_filters.rest_framework import filters
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.order import serializers
from api.order.filters import OrderFilter
from core.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderFilter

    def get_queryset(self):
        return Order.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.OrderSerializerList
        if self.action == "retrieve":
            return serializers.OrderSerializerDetail
        if self.action == "create":
            return serializers.OrderSerializerCreate
        if self.action == 'update':
            return serializers.UnConfirmedOrderSerializerUpdate
        if self.action == 'confirm':
            return serializers.ConfirmUserOrderSerializer
        if self.action == 'deliver':
            return serializers.ConfirmDeliverOrderSerializer
        if self.action == 'cancel':
            return serializers.CancelOrderSerializer

    def confirm(self):
        try:
            serializer = self.get_serializer_class()
            response = serializer.confirm()
            return Response(response)
        except Exception as err:
            return Response(err)

    def deliver(self):
        try:
            serializer = self.get_serializer_class()
            response = serializer.deliver()
            return Response(response)
        except Exception as err:
            return Response(err)

    def cancel(self):
        try:
            serializer = self.get_serializer_class()
            response = serializer.cancel()
            return Response(response)
        except Exception as err:
            return Response(err)
