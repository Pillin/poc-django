from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.forms import ModelMultipleChoiceField, ModelForm
from .models import Reconnaissance
from .resources import ReconnaissanceResource
from speakers.models import Speaker


class ReconnaissanceAdminForm(ModelForm):
    speaker = ModelMultipleChoiceField(
        queryset=Speaker.objects.order_by('name')
    )

    class Meta:
        model = Reconnaissance
        exclude = ('name', 'survey_id')


@admin.register(Reconnaissance)
class ReconnaissanceAdmin(ImportExportModelAdmin):
    resource_class = ReconnaissanceResource
    form = ReconnaissanceAdminForm

    list_display = ('name',  'tendency_raw', 'speakers_raw', 'get_speakers',
                    'mode', 'has_newsletter')
    list_filter = ('gender', 'country', 'speaker__name',
                   'region', 'mode', 'has_newsletter')

    def get_speakers(self, obj):
        return "\n".join([p.name for p in obj.speaker.all()])

    get_speakers.admin_order_field = 'speaker__name'

    def get_queryset(self, request):
        qs = super(ReconnaissanceAdmin, self).get_queryset(request)
        qs = qs.filter(is_disabled=False)
        return qs
