from django.db import models

class GalleryCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = "gallery_categories"
        verbose_name_plural = "Gallery Categories"
        
    def __str__(self):
        return self.name
    
class GalleryImage(models.Model):
    category = models.ForeignKey(
        GalleryCategory, 
        on_delete=models.CASCADE,
        related_name="images"
    )
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="gallery/", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "gallery_images"
        ordering = ["-created_at"]
        
    def __str__(self):
        return f"{self.title} [{self.category.name}]"
    
