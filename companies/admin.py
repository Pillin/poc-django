from django.db.models import Count
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .resources import CompanyResource
from .models import Company

from reconnaissances.models import Reconnaissance


class ReconnaissanceInline(admin.TabularInline):
    model = Reconnaissance.company.through

    fields = ('get_company_raw', 'get_name', "get_link")
    readonly_fields = ('get_company_raw', 'get_name', "get_link")

    def get_company_raw(self, obj):
        return obj.reconnaissance.company_raw

    def get_name(self, obj):
        return obj.reconnaissance.name

    def get_link(self, obj):

        return format_html('<a href="/admin/reconnaissances/reconnaissance/%s/change">%s</a>' % (obj.reconnaissance.id, "Link"))


@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    resource_class = CompanyResource
    list_display = ('name', 'get_recoonaissance_count')
    list_filter = ('name',)

    inlines = [ReconnaissanceInline]

    def get_queryset(self, request):
        qs = super(CompanyAdmin, self).get_queryset(request)
        qs = qs.annotate(Count('reconnaissance'))
        return qs.order_by('-reconnaissance__count')

    def get_recoonaissance_count(self, obj):
        return obj.reconnaissance__count

    get_recoonaissance_count.short_description = 'total'
    get_recoonaissance_count.admin_order_field = 'reconnaissance__count'
