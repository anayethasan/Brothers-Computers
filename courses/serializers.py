from rest_framework import serializers
from courses.models import Course

class CourseListSerializer(serializers.ModelSerializer):
    """Used for course listing page - show short description only."""
    
    class Meta:
        model = Course
        fields = ["id", "title", "price", "description", "duration", "image",]
        
class CourseDetailSerializer(serializers.ModelSerializer):
    """Used for single course detail page - shows full description."""
    
    class Meta:
        model = Course
        fields = [
            "id", "title", "price", "description", "duration", "image", "created_at", "updated_at", 
        ]