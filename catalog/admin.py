from django.contrib import admin

from catalog.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'description')
