from import_export import resources
from import_export.fields import Field
from .models import Company

class CompanyResource(resources.ModelResource):
    count = Field(column_name='total', attribute='get_recoonaissance_count',)

    class Meta:
        model = Company
        fields = ('name', 'count', )
        export_order = ('count', 'name', )


    def dehydrate_count(self, obj):
        return obj.reconnaissance__count