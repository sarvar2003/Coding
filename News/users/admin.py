from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'age', 'is_staff'] 



admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
