from django_filters import rest_framework as filters
from .models import RateHistory

class RateHistoryFilter(filters.FilterSet):
    currency = filters.CharFilter(field_name='currency__code', lookup_expr='iexact')
    start_date = filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')

    class Meta:
        model = RateHistory
        fields = ('currency', 'start_date', 'end_date')