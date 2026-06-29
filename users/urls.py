from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import AdminCreateView, AdminLoginView, AdminLogoutView, ChangePasswordView, AdminProfileView

urlpatterns = [
    path("login/", AdminLoginView.as_view(), name="admin-login"),
    path("logout/", AdminLogoutView.as_view(), name="admin-logout"),
    path("refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("profile/", AdminProfileView.as_view(), name="admin-profile"),
    path("create-admin/", AdminCreateView.as_view(), name="admin-create"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
]
