from import_export.admin import ImportExportModelAdmin
from django.db.models import F, Count

from django.contrib import admin
from django.forms import ModelMultipleChoiceField, ModelForm
from .models import Reconnaissance
from .resources import ReconnaissanceResource
from speakers.models import Speaker
from companies.models import Company


class ReconnaissanceAdminForm(ModelForm):
    speaker = ModelMultipleChoiceField(
        queryset=Speaker.objects.order_by('name'), required=False
    )
    company = ModelMultipleChoiceField(
        queryset=Company.objects.order_by('name'), required=False
    )

    class Meta:
        model = Reconnaissance

        exclude = ('name', 'survey_id')


@admin.register(Reconnaissance)
class ReconnaissanceAdmin(ImportExportModelAdmin):
    resource_class = ReconnaissanceResource
    form = ReconnaissanceAdminForm
    search_fields = ['name', 'speaker__name', ]

    list_display = (
        'name', 'tendency_raw', 'get_companies', 'company_raw', 'get_speakers', 'speakers_raw',
        'mode', 'has_newsletter'
    )

    list_filter = ('seniority', 'gender', 'country',
                   'region', 'mode', 'has_newsletter')

    def get_speakers(self, obj):
        return "\n".join([p.name for p in obj.speaker.all().order_by('name')])

    def get_companies(self, obj):
        return "\n".join([p.name for p in obj.company.all().order_by('name')])

    get_speakers.admin_order_field = 'speaker__name'

    def get_queryset(self, request):
        qs = super(ReconnaissanceAdmin, self).get_queryset(request)
        qs = qs.annotate(c=Count('company')).filter(
            is_disabled=False)
        return qs
