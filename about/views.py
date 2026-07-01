from rest_framework import viewsets
from about.models import AboutSection
from about.serializers import AboutSectionSerializer
from api.permissions import IsAdminOrReadOnly


class AboutSectionViewSet(viewsets.ModelViewSet):
    """
    Visitors can view the about content.
    Only admin can create/update/delete.
    """
    
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    