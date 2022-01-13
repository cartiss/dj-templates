from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе

    class Meta:
        model = StockProduct
        fields = '__all__'

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=True,
    )
    quantity = serializers.IntegerField(min_value=1, default=1)
    price = serializers.DecimalField(min_value=1, decimal_places=2, max_digits=18)


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = '__all__'

    def validate_positions(self, value):
        if not value:
            raise serializers.ValidationError("No position")

        product_ids = [item['products'].id for item in value]

        if len(product_ids) != len(set(product_ids)):
            raise serializers.ValidationError('Дублируются позиции на складе')

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        for item in positions:
            item['stock'] = self.context['request'].user.id

        stock.positions = positions
        stock.save()

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        for item in positions:
            item['stock'] = self.context['request'].user.id

        stock.positions = positions
        stock.save()

        return stock
