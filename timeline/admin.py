from django.contrib import admin
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportMixin
from .models import Timeline

@admin.register(Timeline)
class TimelineAdmin(ImportExportMixin, ModelAdmin):
    list_display = ('event', 'year')
    search_fields = ('event', 'description')
    list_filter = ('year',)
