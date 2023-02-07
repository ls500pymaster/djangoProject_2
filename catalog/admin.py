from django.contrib import admin
from catalog.models import RequestLog, Author, Book, Publisher
from django.utils.translation import ngettext
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse


@admin.register(Author)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publisher", "publication_date", "status")
    list_filter = ("genre", "authors")
    date_hierarchy = "publication_date"
    ordering = ['title']
    actions = ['make_published', 'make_withdrawn']

    @admin.action(description='Mark selected book as published')
    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d book was successfully marked as published.',
            '%d books were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark selected book as withdrawn')
    def make_withdrawn(self, request, queryset):
        updated = queryset.update(status='w')
        self.message_user(request, ngettext(
            '%d book was successfully marked as withdrawn.',
            '%d books were successfully marked as withdrawn.',
            updated,
        ) % updated, messages.SUCCESS)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "country")
    search_fields = ("city", "state_province")


@admin.register(RequestLog)
class LogAdmin(admin.ModelAdmin):
    list_display = ("path", "method", "timestamp", 'status_code', "ip_address")
    list_filter = ("method", "timestamp", "status_code", "ip_address")
    search_fields = ("ip_address", "method")
    date_hierarchy = 'timestamp'
    actions = ['export_as_json']

    @admin.action(description='Export logs in JSON')
    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response, indent=2)
        return
