from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = "product_categories"
        verbose_name_plural = "Product Categories"
        
    def __str__(self):
        return self.name

class Product(models.Model):
    STOCK_CHOICES = (
        ("available", "Available"),
        ("out_of_stock", "Out of Stock"),
    )
    
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(help_text="Supports rich text")
    image = models.ImageField(upload_to="products/")
    stock_status = models.CharField(max_length=15, choices=STOCK_CHOICES, default="available")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "products"
        ordering = ["-created_at"]
        
    def __str__(self):
        return f"{self.name} ({self.get_stock_status_display()})"
    
    @property
    def is_available(self):
        return self.stock_status == "available"
    
