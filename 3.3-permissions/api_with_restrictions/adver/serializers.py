from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from adver.models import Adver


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdverSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Adver
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["creator"] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if instance.creator != self.context['request'].user:
            raise ValidationError('You can\'t update this advert!')

        adver = super().update(instance, validated_data)

        return adver

    def validate(self, data):
        if self.context['request'].method == 'POST' or data.get('status') == 'OPEN':
            if Adver.objects.filter(status='OPEN', creator=self.context['request'].user).count() > 10:
                raise ValidationError("Слишком много объявлений открытых!")

        return data

