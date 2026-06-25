from django.utils import timezone
from django.db import models
 
 
class Notice(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        db_table = "notices"
        ordering = ["-created_at"]
 
    def __str__(self):
        return self.title
 
    @property
    def is_currently_active(self):
        """Returns True if the notice is active and within its time window."""
        now = timezone.now()
        return self.is_active and self.start_time <= now <= self.end_time