from django.contrib import admin

from catalog.models import Course, Version


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('course', 'number_version', 'name', 'is_active', )
