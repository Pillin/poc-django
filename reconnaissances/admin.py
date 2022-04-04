from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Reconnaissance


@admin.register(Reconnaissance)
class PersonAdmin(ImportExportModelAdmin):

    def skip_row(self, instance, original):
        print("Skip row")
        return False
