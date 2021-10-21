# TODO: опишите сериализаторы
from rest_framework.serializers import ModelSerializer
from measurements.models import *


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class MeasurementSerializer(ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"