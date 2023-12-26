from import_export import resources
from import_export.fields import Field
from .models import Speaker

class SpeakerResource(resources.ModelResource):
    count = Field(column_name='total', attribute='get_recoonaissance_count',)

    class Meta:
        model = Speaker
        fields = ('name', 'count', 'twitter', 'youtube', 'twitch', 'linkedin')
        export_order = ('count', 'name', 'twitter', 'youtube', 'twitch', 'linkedin')


    def dehydrate_count(self, obj):
        return obj.reconnaissance__count