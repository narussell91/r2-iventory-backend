from rest_framework import serializers 

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            "product_id",
            "sku",
            "buy_price",
            "listed_price",
            "created_at",
            "buyer_id",
            "store_id",
        )
        model = Product