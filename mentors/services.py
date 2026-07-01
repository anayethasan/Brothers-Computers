from mentors.models import Mentor

class MentorService:
    TOP_COUNT = 3
    
    @staticmethod
    def get_top_mentors():
        """
        Returns the top 3 mentors (is_top=True) for the About page preview
        """
        
        return Mentor.objects.filter(is_top=True)[:MentorService.TOP_COUNT]