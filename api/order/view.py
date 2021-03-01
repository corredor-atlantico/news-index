from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.order import serializers
from api.order.filters import OrderFilter
from core.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
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
        return  serializers.OrderSerializerList

    @action(detail=True, methods=['post'])
    def confirm(self,request, pk=None):
        try:
            serializer = self.get_serializer_class()
            order = self.get_queryset().get(user=pk)
            confirmed = serializer().confirm(order)
            return Response(serializer(confirmed).data)
        except Exception as err:
            return Response(err)

    @action(detail=True, methods=['post'])
    def deliver(self, request, pk=None):
        try:
            serializer = self.get_serializer_class()
            order = self.get_queryset().get(user=pk)
            delivered = serializer().deliver(order)
            return Response(serializer(delivered).data)
        except Exception as err:
            return Response(err)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        try:
            serializer = self.get_serializer_class()
            order = self.get_queryset().get(user=pk)
            cancelled = serializer().cancel(order)
            return Response(serializer(cancelled).data)
        except Exception as err:
            return Response(err)
