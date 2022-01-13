from django_filters import rest_framework as filters

from adver.models import Advertisement


class AdverFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Adver
