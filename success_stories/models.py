from django.db import models

class SuccessStory(models.Model):
    image = models.ImageField(upload_to="success_stories/")
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        db_table = "success_stories"
        verbose_name_plural = "Success Stories"
        ordering = ["-created_at"]
 
    def __str__(self):
        return f"{self.name} — {self.title}"
