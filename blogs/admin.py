from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'header', 'date_create', 'is_published', 'count_views',)
    list_filter = ('date_create', 'is_published',)
    search_fields = ('header', 'content',)
