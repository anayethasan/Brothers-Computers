from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(help_text="short description show on courses after view then show full text")
    
    duration = models.CharField(max_length=100, help_text=" text will this way '3 months'")
    
    image = models.ImageField(upload_to="courses/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "courses"
        ordering = ["-created_at"]
        
    def __str__(self):
        return self.title
    