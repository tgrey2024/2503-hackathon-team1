from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import MentorContact, MentorProfile


@admin.register(MentorProfile)
class MentorProfileAdmin(ModelAdmin):
    """Admin interface for mentor profiles"""

    list_display = ('name', 'role')
    search_fields = ('name', 'role', 'description')


@admin.register(MentorContact)
class MentorContactAdmin(ModelAdmin):
    """Admin interface for mentor contact submissions"""

    list_display = ('mentor_name', 'user', 'submission_status', 'timestamp')
    list_filter = ('submission_status', 'timestamp')
    search_fields = ('mentor_name', 'user__username', 'message')
    readonly_fields = ('timestamp',)
