from rest_framework import viewsets, filters
from shop.models import Product, ProductCategory
from shop.serializers import ProductCategorySerializer, ProductSerializer
from shop.services import ProductService
from api.permissions import IsAdminOrReadOnly
from api.pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend

class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    visitor can browse product categories.
    Only admin can create/update/delete.
    """
    
    queryset = ProductCategory.objects.prefetch_related("products")
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    filter_backends  = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]
    
    
class ProductViewSet(viewsets.ModelViewSet):
    """
    visitor only can view 
    admin create/update/delete
    """
    
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination 
    filterset_fields = ["category", "stock_status"]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["price", "name", "created_at"]
    ordering = ["-created_at"]
    
    def get_queryset(self):
        queryset = Product.objects.select_related("category")

        category_pk = self.kwargs.get("category_pk")
        if category_pk:
            queryset = queryset.filter(category_id=category_pk)

        return queryset
    
    def perform_create(self, serializer):
        category_pk = self.kwargs.get("category_pk")
        if category_pk:
            instance = ProductService.create_product_for_category(category_pk, serializer.validated_data)
            serializer.instance = instance
        else:
            serializer.save()