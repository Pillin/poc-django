from django.db.models import F, Count
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Speaker


@admin.register(Speaker)
class PersonAdmin(ImportExportModelAdmin):

    list_display = ('name', 'twitter', 'youtube', 'twitch', 'get_recoonaissance_count')
    list_filter = ('name', 'twitter', 'youtube', 'twitch',)

    def get_queryset(self, request):
        qs = super(PersonAdmin, self).get_queryset(request)
        qs = qs.annotate(Count('reconnaissance'))
        return qs

    def get_recoonaissance_count(self, obj):
        return obj.reconnaissance__count

    get_recoonaissance_count.short_description = 'total'
    get_recoonaissance_count.admin_order_field = 'reconnaissance__count'
