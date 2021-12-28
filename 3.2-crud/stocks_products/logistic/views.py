from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.paginations import StockProductPagination
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = StockProductPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["positions__id"]
    pagination_class = StockProductPagination
