from django_filters.rest_framework import filters

from core.models import Order


class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = ['deliver_datetime', 'delivered', 'confirmed', 'cancelled', 'recipe', 'user']