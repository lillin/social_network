from django_filters import (
    FilterSet,
    DateFilter
)

from api.models import Like


class DatesRangeFilter(FilterSet):
    date_from = DateFilter(field_name='date', lookup_expr='gte')
    date_to = DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Like
        fields = ['date_from', 'date_to', ]
