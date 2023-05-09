from rest_framework import serializers

from catalogue.models import Brand, Product
from warehouse.models import WarehouseItem
from warehouse.serializers import WarehouseItemSerializer


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "article",
            "name",
            "brand",
            "description",
            "price",
            "size",
            "gender",
            "type",
            "image_url"
        )

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        else:
            return None

    def get_price(self, obj):
        try:
            warehouse_item = WarehouseItem.objects.get(product=obj)
            return warehouse_item.sale_price
        except WarehouseItem.DoesNotExist:
            return None

    def get_brand(self, obj):
        return obj.brand.name


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
