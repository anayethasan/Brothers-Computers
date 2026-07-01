from rest_framework import viewsets, filters
from courses.models import Course
from courses.serializers import CourseDetailSerializer, CourseListSerializer
from api.permissions import IsAdminOrReadOnly


class CourseViewSet(viewsets.ModelViewSet):
    """
    visitors can browse all courses list and view a single course details.
    Only admin can create/update/delete.
    """
    
    queryset = Course.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    
    def get_serializer_class(self):
        if self.action == "list":
            return CourseListSerializer
        return CourseDetailSerializer
    
    
