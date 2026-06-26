from rest_framework import serializers
from banners.models import Banner

class BannerSerializer(serializers.ModelSerializer):
    page_name_display = serializers.CharField(source="get_page_name_display", read_only=True)
    
    class Meta:
        model = Banner
        fields = ["id","page_name", "page_name_display", "title", "image",]