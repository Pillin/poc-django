
from import_export import resources
from .models import Reconnaissance


class ReconnaissanceResource(resources.ModelResource):

    class Meta:
        model = Reconnaissance
