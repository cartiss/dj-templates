from django_filters import rest_framework as filters, DateFromToRangeFilter

from adver.models import Adver


class AdverFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter()

    class Meta:
        model = Adver
        fields = ('created_at', 'status')
