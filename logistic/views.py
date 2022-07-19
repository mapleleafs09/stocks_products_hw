from django.http import HttpResponse
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

import logistic
from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации



class StockViewSet(ModelViewSet):
    def get_queryset(self):
        if self.request.GET != {}:
            product_name = self.request.GET.get('products', '')
            try:
                product_id = Product.objects.get(title__icontains=product_name)
            except logistic.models.Product.DoesNotExist:
                pass
            try:
                product_id = Product.objects.get(description__icontains=product_name)
            except logistic.models.Product.DoesNotExist:
                product_id = product_name
            return Stock.objects.filter(products=product_id)
        else:
            return Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = LimitOffsetPagination

    # при необходимости добавьте параметры фильтрации

