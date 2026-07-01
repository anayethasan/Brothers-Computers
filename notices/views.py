from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from notices.models import Notice
from notices.serializers import NoticeSerializer
from notices.services import NoticeService
from api.permissions import IsAdminOrReadOnly
from api.pagination import DefaultPagination

class NoticeViewSet(viewsets.ModelViewSet):
    """
    Visitors can browse all notices.
    Only admin can create/update/delete.
    """
    
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination
    ordering_fields = ["start_time", "end_time", "created_at"]
    ordering = ["-created_at"]
    
    @action(detail=False, methods=["get"], url_path="active")
    def active_notices(self, request):
        """
        GET /api/notices/active/
        Returns only notices that are currently active.
        """
        notices = NoticeService.get_active_notices()
        serializer = self.get_serializer(notices, many=True)
        return Response(serializer.data)