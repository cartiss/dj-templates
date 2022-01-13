from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from adver.models import Adver
from adver.serializers import AdverSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Adver.objects.all()
    serializer_class = AdverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at', 'status']
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAuthenticated()]
        return []