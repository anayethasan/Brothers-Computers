from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from mentors.models import Mentor
from mentors.serializers import MentorSerializer
from mentors.services import MentorService
from api.permissions import IsAdminOrReadOnly
from api.pagination import DefaultPagination

class MentorViewSet(viewsets.ModelViewSet):
    """
    Visitor can browse all mentors 
    only admin can create/update/delete
    """
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination
    ordering = ["-is_top", "name"]
    
    @action(detail=False, methods=["get"], url_path="top")
    def top_mentors(self, request):
        """
        Get/api/mentors/top
        Returns the top 3 mentors for the about page preview.
        """
        mentors = MentorService.get_top_mentors()
        serializer = self.get_serializer(mentors, many=True)
        return Response(serializer.data)
    