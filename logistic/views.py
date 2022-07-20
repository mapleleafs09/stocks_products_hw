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
            products_ids = set()
            product_name = self.request.GET.get('products', '')
            try:
                ids = [product_id.id for product_id in
                               Product.objects.filter(title__icontains=product_name)]
                products_ids.update(ids)
            except logistic.models.Product.DoesNotExist:
                pass
            try:
                ids = [product_id.id for product_id in
                               Product.objects.filter(description__icontains=product_name)]

                products_ids.update(ids)
            except logistic.models.Product.DoesNotExist:
                pass
            try:

                ids = [product_id.id for product_id in
                       Product.objects.filter(id__icontains=product_name)]
                products_ids.update(ids)
            except logistic.models.Product.DoesNotExist:
                pass
            print(products_ids)
            return Stock.objects.filter(products__in=products_ids)
        else:
            return Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = LimitOffsetPagination

    # при необходимости добавьте параметры фильтрации

