from rest_framework import viewsets, filters
from success_stories.models import SuccessStory
from success_stories.serializers import SuccessStorySerializer
from api.permissions import IsAdminOrReadOnly
from api.pagination import DefaultPagination


class SuccessStoryViewSet(viewsets.ModelViewSet):
    """
    Visitors can browse all success stories.
    Only admin can create/update/delete.
    """
    
    queryset = SuccessStory.objects.all()
    serializer_class = SuccessStorySerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    search_fields = ["name", "title"]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]
    