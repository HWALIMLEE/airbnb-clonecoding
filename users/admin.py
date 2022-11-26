from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# 꼭 모델 안에 존재해야 하는 필드들이어야 함
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Profile", {"fields": (
            "username", "password", "name", "email", "is_host"
        ), "classes": ("wide",)},),
        ("Permission", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            ),
            "classes": ("collapse",),
        },),
        ("Important Dates", {"fields": ("last_login", "date_joined"),
                             "classes": ("collapse",)}),
    )
    list_display = ("username", "email", "name", "is_host")