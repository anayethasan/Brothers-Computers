from django.db import models
 
 
class Testimonial(models.Model):
    RATTING_CHOICES = [(i, str(i)) for i in range(1, 6)]
 
    image = models.ImageField(upload_to="testimonials/")
    title = models.CharField(max_length=250, help_text="Short headline for the testimonial")
    rating = models.PositiveSmallIntegerField(choices=RATTING_CHOICES, default=5)
    description = models.TextField()
 
    name = models.CharField(max_length=150, help_text="Reviewer's name")
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        db_table = "testimonials"
        ordering = ["-created_at"]
 
    def __str__(self):
        return f"{self.name} - {self.title}"