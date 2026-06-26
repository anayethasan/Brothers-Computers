from rest_framework import serializers
from mentors.models import Mentor

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ["id", "name", "designation", "image", "bio", "is_top", "created_at",]
        read_only_fields = ["id", "created_at"]
        
        
        