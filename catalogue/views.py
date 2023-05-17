from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from catalogue.models import Brand, Product
from catalogue.serializers import BrandSerializer, ProductSerializer, ProductItemsSerializer
from user.permissions import IsAdmin
from warehouse.models import WarehouseItem


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
    queryset = Product.objects.select_related("brand").all()
    serializer_class = ProductSerializer
    permission_classes_per_method = {
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
        "items": [AllowAny],
        "item": [AllowAny],
    }

    def get_permissions(self):
        permission_classes = self.permission_classes_per_method.get(self.action, [IsAdmin])
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["items", "item"]:
            queryset = Product.objects.select_related("brand").prefetch_related(
                Prefetch(
                    "warehouse_items",
                    queryset=WarehouseItem.objects.filter(quantity__gt=0).order_by("-date")[:1],
                    to_attr="resent_item"
                )
            )
        return queryset

    def get_serializer_class(self):
        if self.action in ["items", "item"]:
            return ProductItemsSerializer
        return ProductSerializer

    @action(detail=False, methods=["get"])
    def items(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def item(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer(product)
        return Response(serializer.data)
