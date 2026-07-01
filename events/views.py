from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from events.models import Event
from events.services import EventService
from events.serializers import EventSerializer
from api.permissions import IsAdminOrReadOnly
from api.pagination import DefaultPagination

class EventViewSet(viewsets.ModelViewSet):
    """
    Visitors can browse all events.
    only admin can create/update/delete.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPagination
    
    @action(detail=False, methods=["get"], url_path="latest")
    def latest_events(self, request):
        """
        Returns the latest 2 events for the home page
        """
        events = EventService.get_latest_events()
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
    
    