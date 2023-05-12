from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from catalogue.models import Brand, Product
from catalogue.serializers import BrandSerializer, ProductSerializer, ProductDetailSerializer
from user.permissions import IsAdmin


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes_per_method = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser]
    }

    def get_permissions(self):
        permission_classes = self.permission_classes_per_method.get(self.action, [IsAdmin])
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        return BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes_per_method = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser]
    }

    def get_permissions(self):
        permission_classes = self.permission_classes_per_method.get(self.action, [IsAdmin])
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return ProductDetailSerializer
        return ProductSerializer
