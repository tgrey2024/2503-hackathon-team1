from django.contrib import admin
from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin
from .models import Timeline, Honour

@admin.register(Timeline)
class TimelineAdmin(ImportExportMixin, ModelAdmin):
    """Interface for Timeline model"""
    list_display = ('event', 'year', 'honour_count')
    search_fields = ('event', 'description')
    list_filter = ('year',)

    def honour_count(self, obj):
        return obj.honours.count()
    honour_count.short_description = 'Honours'

@admin.register(Honour)
class HonourAdmin(ModelAdmin):
    """Interface for Honour model"""
    list_display = ('user', 'timeline', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'timeline__event')
