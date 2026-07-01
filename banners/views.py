from rest_framework import viewsets, filters
from banners.models import Banner
from banners.serializers import BannerSerializer
from api.permissions import IsAdminOrReadOnly

class BannerViewSet(viewsets.ModelViewSet):
    """
    Visitors can view all banners.
    only admin can create/update/delete.
    """
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
    