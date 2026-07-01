from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="events/", null=True)
    time = models.CharField(
        max_length=100,
        help_text='Free-text time "Sunday 2 PM to 4 PM"'
    )
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        db_table = "events"
        ordering = ["-created_at"]
 
    def __str__(self):
        return self.title
