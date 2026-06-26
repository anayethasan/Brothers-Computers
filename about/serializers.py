from rest_framework import serializers
from about.models import AboutSection

class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = ["id", "title", "description", "image", "secondary_image"]