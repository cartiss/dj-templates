from django_filters import rest_framework as filters, DateFromToRangeFilter

from adver.models import Adver


class AdverFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    date = DateFromToRangeFilter()

    class Meta:
        model = Adver
        fields = ('date', 'status')
