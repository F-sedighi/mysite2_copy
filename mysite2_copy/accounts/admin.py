# Register your models here.
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import EmailCreationForm
 

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'date_joined', 'is_staff']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email', 'username']
    ordering = ['email']
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'username', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(User, CustomUserAdmin)

