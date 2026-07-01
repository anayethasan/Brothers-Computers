from rest_framework import viewsets, filters
from gallery.models import GalleryCategory, GalleryImage
from gallery.serializers import (GalleryCategorySerializer, GalleryCategoryWithImagesSerializer, GalleryImageSerializer)
from gallery.services import GalleryService
from api.permissions import IsAdminOrReadOnly
from api.pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend

class GalleryCategoryViewSet(viewsets.ModelViewSet):
    """
    Visitors can browse categories (with their image nested, for the category filter UI). Only admin can create/update/delete categories.
    """
    queryset = GalleryCategory.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    
    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return GalleryCategoryWithImagesSerializer
        return GalleryCategorySerializer
    
class GalleryImageViewSet(viewsets.ModelViewSet):
    """
    (nested images under one category)
    """
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    filterset_fields = ["category"]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title"]
    ordering_fields = ["created_at", "title"]
    ordering = ["-created_at"]
    
    def get_queryset(self):
        category_pk = self.kwargs.get("category_pk")
        if category_pk:
            return GalleryService.get_images_for_category(category_pk)
        return GalleryService.get_images()
    
    def perform_create(self, serializer):
        category_pk = self.kwargs.get("category_pk")
        if category_pk:
            instance = GalleryService.create_image_for_category(category_pk, serializer.validated_data)
            serializer.instance = instance
        else:
            serializer.save()
            
