from gallery.models import GalleryCategory, GalleryImage

class GalleryService:
    
    @staticmethod
    def get_images():
        return GalleryImage.objects.select_related("category")
    
    @staticmethod
    def get_images_for_category(category_pk):
        """
        Returns all images belonging to a specific category.
        """
        return (
            GalleryImage.objects.select_related("category").filter(category_id=category_pk)
        )
    
    @staticmethod
    def create_image_for_category(category_pk, validated_data):
        """
        Validates the category exists, then creates the image under it.
        """
        category = GalleryCategory.objects.get(pk=category_pk)
        return GalleryImage.objects.create(category=category, **validated_data)