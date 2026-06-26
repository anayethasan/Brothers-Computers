from django.db import models
 
 
class AboutSection(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="about/")
    secondary_image = models.ImageField(upload_to="about/",  null=True, blank=True)
 
    class Meta:
        db_table = "about_sections"
 
    def __str__(self):
        return self.title