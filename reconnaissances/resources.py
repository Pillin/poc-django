
from django.db import IntegrityError
from import_export import resources
from .models import Reconnaissance


class ReconnaissanceResource(resources.ModelResource):

    class Meta:
        model = Reconnaissance
        skip_unchanged = True
        report_skipped = True

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        try:
            super(ReconnaissanceResource, self).save_instance(
                instance, using_transactions, dry_run)
        except IntegrityError:
            pass
