from django.db.models import F, Count, Value, IntegerField
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Speaker
from reconnaissances.models import Reconnaissance
from .resources import SpeakerResource


class ReconnaissanceInline(admin.TabularInline):
    model = Reconnaissance.speaker.through

    fields = ('get_speakers_raw', 'get_name', "get_link")
    readonly_fields = ('get_speakers_raw', 'get_name', "get_link")

    def get_speakers_raw(self, obj):
        return obj.reconnaissance.speakers_raw

    def get_name(self, obj):
        return obj.reconnaissance.name

    def get_link(self, obj):
        return format_html('<a href="/admin/reconnaissances/reconnaissance/%s/change">%s</a>' % (obj.reconnaissance.id, "Link"))


@admin.register(Speaker)
class PersonAdmin(ImportExportModelAdmin):
    resource_class = SpeakerResource

    list_display = ('name', 'twitter', 'youtube', 'twitch',
                    'get_recoonaissance_count', 'get_percentage_reconnaissance')
    list_filter = ('name', 'twitter', 'youtube', 'twitch',)
    inlines = [ReconnaissanceInline]

    def get_queryset(self, request):
        qs = super(PersonAdmin, self).get_queryset(request)
        reconnaissance_total = Reconnaissance.objects.filter(
            speaker__gt=1).count()
        qs = qs.annotate(Count('reconnaissance')).annotate(
            reconnaissance_total=Value(reconnaissance_total, IntegerField()))
        return qs.order_by('-reconnaissance__count')

    def get_recoonaissance_count(self, obj):
        return obj.reconnaissance__count

    get_recoonaissance_count.short_description = 'total'
    get_recoonaissance_count.admin_order_field = 'reconnaissance__count'

    def get_percentage_reconnaissance(self, obj):
        return '{0:.3g}'.format(obj.reconnaissance__count*100 / obj.reconnaissance_total)

    get_percentage_reconnaissance.short_description = 'Percentage'
