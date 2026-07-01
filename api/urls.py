from django.urls import path, include

from rest_framework_nested import routers 
from testimonials.views import TestimonialViewSet
from success_stories.views import SuccessStoryViewSet
from shop.views import ProductViewSet, ProductCategoryViewSet
from notices.views import NoticeViewSet
from mentors.views import MentorViewSet
from home.views import HomeHeroViewSet, HomeVideoViewSet

router = routers.DefaultRouter()
router.register("testimonials", TestimonialViewSet, basename="testimonials")
router.register("success_stories", SuccessStoryViewSet, basename="success-stories")
router.register("notices", NoticeViewSet, basename="notices")
router.register("mentors", MentorViewSet, basename="mentors")
router.register("carousel", HomeHeroViewSet, basename="carousel")
router.register("home-videos", HomeVideoViewSet, basename="home-videos")

#nested router base
router.register("categories", ProductCategoryViewSet, basename="categories")
router.register("products", ProductViewSet, basename="products")

#nested router
product_router = routers.NestedDefaultRouter(router, "categories", lookup="category")
product_router.register("products", ProductViewSet, basename="category-products")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_router.urls)),
    
    path('auth/', include('users.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
