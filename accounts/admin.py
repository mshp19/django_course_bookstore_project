from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    List_display=['Username','email','is_staff','age',]
    fieldsets = UserAdmin.fieldsets+(
        (None, {'fields':('age',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
