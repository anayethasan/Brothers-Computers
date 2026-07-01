from rest_framework import serializers
from shop.models import ProductCategory, Product


 
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    is_available = serializers.BooleanField(read_only=True)
    stock_status_display = serializers.CharField(source="get_stock_status_display", read_only=True)
 
    class Meta:
        model = Product
        fields = [
            "id", "category", "category_name", "name", "price",
            "description", "image", "stock_status", "stock_status_display",
            "is_available", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

class ProductCategorySerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = ProductCategory
        fields = ["id", "name"]
 