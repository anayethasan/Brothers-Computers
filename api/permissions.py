from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Visitors (no login required) can only read (GET, HEAD, OPTIONS).
    Only authenticated admin users (is_staff=True) can create, update, or delete.

    This is the default permission for almost every public-facing app
    (banners, home, about, courses, mentors, testimonials, gallery, shop,
    notices, success_stories, events).
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
