from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Profile, Qweet


class ProfileInLine(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInLine]


admin.site.unregister(Group)
admin.site.register(Qweet)
