from rest_framework import viewsets

from catalogue.models import Brand, Product
from catalogue.serializers import BrandSerializer, ProductSerializer, ProductDetailSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return ProductDetailSerializer
        return ProductSerializer
