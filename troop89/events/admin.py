from django.contrib import admin
from .models import Event, EventType

from markdownx.admin import MarkdownxModelAdmin

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(MarkdownxModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = ('title', 'type', 'start', 'end')

    list_filter = ('type', 'start')

    date_hierarchy = 'start'

    fieldsets = (
        (None, {
            'fields': ('title', 'type', 'description', 'start', 'end')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('slug',)
        })
    )