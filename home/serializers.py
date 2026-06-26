from rest_framework import serializers
from home.models import HomeHero, HomeVideo

class HomeHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHero
        fields = ["id", "title", "subtitle", "image", "index",]
        

class HomeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeVideo
        fields = ["id", "youtube_url", "created_at"]
        read_only_fields = ["id", "created_at"]