from django.http import HttpResponse
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['title']
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации



class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filterset_fields = ['products']
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['address']
    # при необходимости добавьте параметры фильтрации

