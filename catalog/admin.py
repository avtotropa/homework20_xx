from django.contrib import admin

from catalog.models import Course, Version
from users.models import User


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('course', 'number_version', 'name', 'is_active',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'country', 'phone', )
