from rest_framework.exceptions import ValidationError
from home.models import HomeHero

class HomeHeroServices:
    MAX_SLIDES = 3
    
    @staticmethod
    def create_slide(validated_data):
        """
        only 2 hero carousel slides allowed.
        Raise validationError if the limit is already reached.
        """
        
        if HomeHero.objects.count() >= HomeHeroServices.MAX_SLIDES:
            raise ValidationError({"detail": f"only {HomeHeroServices.MAX_SLIDES} hero slides are allowed" f"Delete one before adding a new slide."})
        return HomeHero.objects.create(**validated_data)
    