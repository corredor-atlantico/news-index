from rest_framework import serializers

from core.models import Order


class OrderSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'deliver_datetime']


class OrderSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['deliver_datetime', 'deliver_address', 'deliver_notes', 'recipe']


class OrderSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['deliver_datetime', 'deliver_address', 'deliver_notes', 'recipe']


class UnConfirmedOrderSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['deliver_datetime', 'deliver_address', 'deliver_notes', 'recipe']


class ConfirmedOrderSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['deliver_address', 'deliver_notes', ]


class ConfirmUserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['confirmed', ]

    def confirm(self, instance):
        if not instance.confirmed:
            instance.confirmed = True
            instance.save()
            return instance
        else:
            return None


class ConfirmDeliverOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['delivered', ]

    def deliver(self, instance):
        if not instance.delivered:
            instance.delivered = True
            instance.save()
            return instance
        else:
            return None


class CancelOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['cancelled', ]

    def cancel(self, instance):
        if not instance.cancelled:
            instance.cancelled = True
            instance.save()
            return instance
        else:
            return None
