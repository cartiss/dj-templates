from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from adver.filters import AdverFilter
from adver.models import Adver
from adver.serializers import AdverSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Adver.objects.all()
    serializer_class = AdverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdverFilter
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsAuthenticated()]
        return []

    def destroy(self, request, *args, **kwargs):
        if request.user != self.get_object().creator:
            return Response("Вы не можете удалять это объявление", status=403)

        return super().destroy(request, *args, **kwargs)




