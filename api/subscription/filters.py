from django_filters.rest_framework import filters

from core.models import Subscription


class SubscriptionFilter(filters.FilterSet):
    class Meta:
        model = Subscription
        fields = ['type', 'start_date', 'end_date', 'user']