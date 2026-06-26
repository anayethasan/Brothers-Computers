from rest_framework import serializers
from notices.models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    is_currently_active = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Notice
        fields = [
            "id", "title", "description", "is_active", "start_time", "end_time", "is_currently_active", "created_at",
        ]
        read_only_fields = ["id", "created_at"]