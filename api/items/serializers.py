from rest_framework import serializers

from core.models import Items


class ItemSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['name', 'type.description']


class ItemSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['name', 'stock_amount', 'order_amount', 'type', 'cost']


class ItemSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['name', 'stock_amount', 'order_amount', 'type', 'cost']


class ItemSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['name', 'stock_amount', 'order_amount', 'type', 'cost']
