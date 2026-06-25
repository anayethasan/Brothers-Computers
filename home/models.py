from django.db import models

class HomeHero(models.Model):
    title = models.CharField(max_length=260)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="home/heroes")
    index = models.PositiveSmallIntegerField(default=0, help_text="Carousel order. it is 0 indexing so 0 mean first banner")
    
    class Meta:
        db_table = "home_heroes"
        ordering = ["index"]
        
    def __str__(self):
        return f"Hero Slide {self.index} - {self.title}"
    

class HomeVideo(models.Model):
    youtube_url = models.URLField(help_text="Full YouTube video URL")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "home_videos"
        ordering = ["-created_at"]
        
    def __str__(self):
        return f"Video - {self.youtube_url}"
    
