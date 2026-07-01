from rest_framework import viewsets, filters
from testimonials.models import Testimonial 
from testimonials.serializers import TestimonialSerializer
from api.permissions import IsAdminOrReadOnly
from api.pagination import DefaultPagination

class TestimonialViewSet(viewsets.ModelViewSet):
    
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "title"]
    ordering_fields = ["rating", "created_at"]
    ordering = ["-created_at"]
    
    