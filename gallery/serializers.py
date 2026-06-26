from rest_framework import serializers
from gallery.models import GalleryCategory, GalleryImage

class GalleryImageSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    
    class Meta:
        model = GalleryImage
        fields = ["id", "category", "category_name", "title", "image", "created_at"]
        read_only_fields = ["id", "created_at"]
        
class GalleryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = ["id", "name"]
 
 
class GalleryCategoryWithImagesSerializer(serializers.ModelSerializer):
    """when you want a category and all its images together."""
    images = GalleryImageSerializer(many=True, read_only=True)
 
    class Meta:
        model = GalleryCategory
        fields = ["id", "name", "images"]