from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
 
 
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
 
    list_display = (
        "email",
        "name",
        "is_active",
        "is_staff",
        "date_joined",
    )
 
    list_filter = (
        "is_staff",
        "is_active",
    )
 
    search_fields = (
        "email",
        "name",
    )
 
    ordering = ("email",)
 
    fieldsets = (
        (None, {
            "fields": ("email", "password")
        }),
        ("Personal Info", {
            "fields": ("name", "image")
        }),
        ("Permissions", {
            "fields": (
                "is_staff",
                "is_active",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important Dates", {
            "fields": (
                "last_login",
                "date_joined",
            )
        }),
    )
 
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "name",
                "image",
                "password1",
                "password2",
                "is_staff",
                "is_active",
            ),
        }),
    )
 
    readonly_fields = (
        "date_joined",
        "last_login",
    )