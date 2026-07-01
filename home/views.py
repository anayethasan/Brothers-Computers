from rest_framework import viewsets
from home.models import HomeHero, HomeVideo
from home.serializers import HomeHeroSerializer, HomeVideoSerializer
from home.services import HomeHeroServices
from api.permissions import IsAdminOrReadOnly

class HomeHeroViewSet(viewsets.ModelViewSet):
    """
    visitors see the hero carousel ordered by index
    admin can manage slides
    """
    
    queryset = HomeHero.objects.all()
    serializer_class = HomeHeroSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    
    def perform_create(self, serializer):
        instance = HomeHeroServices.create_slide(serializer.validated_data)
        serializer.instance = instance
        

class HomeVideoViewSet(viewsets.ModelViewSet):
    """
        visitors see uploaded Youtube Video links.
        admin can post/delete video links.
    """
    
    queryset = HomeVideo.objects.all()
    serializer_class = HomeVideoSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    
    