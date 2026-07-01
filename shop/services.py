from shop.models import Product, ProductCategory

class ProductService:
    @staticmethod
    def get_products_for_category(category_pk):
        """
        Returns all Products beloging to a specific category.
        """
        return  Product.objects.select_related("category").filter(category_id=category_pk)
    
    @staticmethod
    def create_product_for_category(category_pk, validated_data):
        category = ProductCategory.objects.get(pk=category_pk)
        return Product.objects.create(category=category, **validated_data)
    