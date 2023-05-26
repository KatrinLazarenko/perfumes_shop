from django.db.models import Prefetch, Model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from catalogue.models import Brand, Product
from catalogue.serializers import BrandSerializer, ProductSerializer, ProductItemsSerializer, ProductDetailSerializer
from user.permissions import IsAdmin
from warehouse.models import WarehouseItem

from django.core.exceptions import ObjectDoesNotExist


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
    ordering = ["brand"]
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
        if self.action in ["list", "retrieve"]:
            queryset = Product.objects.select_related("brand").order_by(*self.ordering)
            return queryset
        return self.queryset

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductSerializer
        if self.action in ["items", "item"]:
            return ProductItemsSerializer
        return ProductDetailSerializer

    def __prefetch_recent_item(self, queryset):
        queryset = Product.objects.select_related("brand").prefetch_related(
            Prefetch(
                "warehouse_items",
                queryset=WarehouseItem.objects.filter(quantity__gt=0).order_by("-date")[:1],
                to_attr="resent_item"
            )
        )
        return queryset
    def __filter_by_brand(self, request, queryset):
        brand = request.query_params.get("brand")
        if brand:
            queryset = queryset.filter(brand=brand)
        return queryset

    def __filter_by_name(self, request, queryset):
        name = request.query_params.get("name")
        if name:
            queryset = queryset.filter(name=name)
        return queryset

    def __filter_by_gender(self, request, queryset):
        gender = request.query_params.get("gender")
        if gender:
            queryset = queryset.filter(gender=gender)
        return queryset

    def __filter_by_type(self, request, queryset):
        item_type = request.query_params.get("type")
        if item_type:
            queryset = queryset.filter(type=item_type)
        return queryset


    @action(detail=False, methods=["get"])
    def items(self, request):
        queryset = self.__prefetch_recent_item(self.queryset)
        queryset = self.__filter_by_brand(request, queryset)
        queryset = self.__filter_by_name(request, queryset)
        queryset = self.__filter_by_gender(request, queryset)
        queryset = self.__filter_by_type(request, queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def item(self, request, pk=None):
        queryset = self.__prefetch_recent_item(self.queryset)
        try:
            product = queryset.get(id=int(pk))
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response("Item not found", status=status.HTTP_404_NOT_FOUND)
