from django.urls import path, include

from rest_framework_nested import routers 
from testimonials.views import TestimonialViewSet
from success_stories.views import SuccessStoryViewSet
from shop.views import ProductViewSet, ProductCategoryViewSet
from notices.views import NoticeViewSet
from mentors.views import MentorViewSet
from home.views import HomeHeroViewSet, HomeVideoViewSet
from gallery.views import GalleryCategoryViewSet, GalleryImageViewSet
from events.views import EventViewSet
from courses.views import CourseViewSet
from banners.views import BannerViewSet
from about.views import AboutSectionViewSet

router = routers.DefaultRouter()
router.register("testimonials", TestimonialViewSet, basename="testimonials")
router.register("success_stories", SuccessStoryViewSet, basename="success-stories")
router.register("notices", NoticeViewSet, basename="notices")
router.register("mentors", MentorViewSet, basename="mentors")
router.register("carousel", HomeHeroViewSet, basename="carousel")
router.register("home-videos", HomeVideoViewSet, basename="home-videos")
router.register("events", EventViewSet, basename="events")
router.register("courses", CourseViewSet, basename="courses")
router.register("banners", BannerViewSet, basename="banners")
router.register("about", AboutSectionViewSet, basename="about")

#nested router base
router.register("categories", ProductCategoryViewSet, basename="categories")
router.register("products", ProductViewSet, basename="products")
router.register("image-categories", GalleryCategoryViewSet, basename="image-categories")
router.register("images", GalleryImageViewSet, basename="images")

#nested router
product_router = routers.NestedDefaultRouter(router, "categories", lookup="category")
product_router.register("products", ProductViewSet, basename="category-products")

image_router = routers.NestedDefaultRouter(router, "image-categories", lookup="category")
image_router.register("images", GalleryImageViewSet, basename="category-images")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_router.urls)),
    
    path('auth/', include('users.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
