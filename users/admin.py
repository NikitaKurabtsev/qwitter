from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
 
from qwitter_app.models import Profile
from users.models import CustomUser
from users.forms import CustomUserCreationForm, CustomUserChangeForm


class ProfileInLine(admin.StackedInline):
    model = Profile


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    inlines = [ProfileInLine]
    list_display = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
