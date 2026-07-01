from django.utils import timezone
from notices.models import Notice


class NoticeService:
    @staticmethod
    def get_active_notices():
        """
        Returns notices that are currently active:
        is_active=True AND now is within [start_time, end_time].
        Used by the frontend notice bar (auto show/hide logic).
        """
        now = timezone.now()
        return Notice.objects.filter(
            is_active=True,
            start_time__lte=now,
            end_time__gte=now,
        )