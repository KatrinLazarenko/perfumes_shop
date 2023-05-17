from rest_framework import serializers

from catalogue.models import Brand, Product


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_brand(self, obj):
        return obj.brand.name


class ProductItemsSerializer(serializers.ModelSerializer):
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
            return obj.resent_item[0].sale_price
        except IndexError:
            return "Out of stock"

    def get_brand(self, obj):
        return obj.brand.name
