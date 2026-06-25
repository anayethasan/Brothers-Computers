from django.db import models


class Banner(models.Model):
    PAGE_CHOICES = (
        ("ABOUT", "About"),
        ("COURSES", "Courses"),
        ("GALLERY", "Gallery"),
        ("SHOP", "Shop"),
        ("CONTACT", "Contact"),
        ("MENTOR", "Mentor"),
        ("SUCCESS_STORY", "Success Story"),
        ("EVENT", "Event"),
    )
    page_name = models.CharField(max_length=30, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=260)
    image = models.ImageField(upload_to="banners/")
    
    class Meta:
        db_table = "banners"
        
    def __str__(self):
        return f"Banner - {self.get_page_name_display()}"
    
