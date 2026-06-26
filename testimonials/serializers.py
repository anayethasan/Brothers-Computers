from rest_framework import serializers
from testimonials.models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            "id", "image", "title", "rating", "description", 
            "name", "created_at",
        ]
        read_only_fields = ["id", "created_at"]