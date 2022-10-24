from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    """Customized UserAdmin which includes the modified User model's slug field, and also has rearranged fieldsets"""
    list_display = ("username", "email", "slug", "first_name", "last_name", "is_staff")
    fieldsets = (
        (None, 
        {
            "fields": (
                "username",
                "password",
                "slug",
                ),
        },
        ),

        (("Personal info"),
        {
            "fields": (
                "first_name",
                "last_name",
                "email",
                ),
        },
        ),

        (("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),

        (("Important dates"), 
        {
            "fields": (
                "last_login",
                "date_joined",
                ),
        },
        ),
    )


admin.site.register(User, CustomUserAdmin)