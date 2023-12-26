from django.core.management.base import BaseCommand
from reconnaissances.models import Reconnaissance
from companies.models import Company


def add_companies():
    companies = Company.objects.all()
    proccess_count = 0
    for company in companies:
        all_reconnaissances = Reconnaissance.objects.filter(
            company_raw__icontains=company.name)

        for reconnaissance in all_reconnaissances:
            reconnaissance.company.add(company)
            reconnaissance.save()
            proccess_count += 1

    print(proccess_count)


class Command(BaseCommand):
    def handle(self, **options):
        add_companies()
