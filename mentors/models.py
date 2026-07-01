from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to="mentors/", null=True)
    bio = models.TextField()
    is_top = models.BooleanField(
        default=False,
        help_text="Mark as Top Mentor to show on the about page preview"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "mentors"
        ordering = ["-is_top", "name"]
        
    def __str__(self):
        return f"{self.name} - {self.designation}"
    
    
