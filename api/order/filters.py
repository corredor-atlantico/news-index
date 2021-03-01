from django_filters.rest_framework import FilterSet

from core.models import Order


class OrderFilter(FilterSet):
    class Meta:
        model = Order
        fields = ['deliver_datetime', 'delivered', 'confirmed', 'cancelled', 'recipe', 'user']