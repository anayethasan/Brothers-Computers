from events.models import Event

class EventService:
    LATEST_COUNT = 2
    
    @staticmethod
    def get_latest_events():
        """
        Returns the latest 2 events for the Home
        Page preview section.
        """
        return Event.objects.all()[:EventService.LATEST_COUNT]