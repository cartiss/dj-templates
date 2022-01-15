from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
        fields = ['product', 'quantity', 'price']

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

        product_ids = [item['product'].id for item in value]

        if len(product_ids) != len(set(product_ids)):
            raise serializers.ValidationError('Дублируются позиции на складе')

        return value

    def create(self, validated_data):
        stock = super().create(validated_data)

        for item in stock.positions:
            item['stock'] = stock.id

        stock.save()

        return stock

    def update(self, instance, validated_data):

        if not instance:
            return ValidationError('Bad request (no object)')

        instance.address = validated_data.get('address', instance.address)
        instance.positions = validated_data.get('positions', instance.positions)

        stock = super().update(instance, validated_data)

        for item in stock.positions:
            item['stock'] = stock.id

        stock.save()

        return stock
