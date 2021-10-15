# TODO: опишите сериализаторы
from rest_framework.serializers import ModelSerializer
from measurements.models import *


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "name, updated_at"

class MeasurementSerializer(ModelSerializer):
    class Meta:
        model = Measurement
        fields = "value, project, updated_at"