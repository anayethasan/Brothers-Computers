from rest_framework import serializers
from success_stories.models import SuccessStory

class SuccessStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStory
        fields = ["id", "image", "name", "title", "description", "created_at"]
        read_only_fields = ["id", "created_at"]