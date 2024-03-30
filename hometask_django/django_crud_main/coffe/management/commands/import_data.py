import csv
from decimal import Decimal
from django.core.management.base import BaseCommand
from coffe.models import Coffee


class Command(BaseCommand):
    help = 'Import coffee prices from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import.')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                Coffee.objects.create(
                    drink_type=row['drink_type'],
                    price_small=Decimal(row['price_small']),
                    price_medium=Decimal(row['price_medium']),
                    price_large=Decimal(row['price_large'])
                )

# python manage.py import_data "C:\python\hometask_django\prices.csv"
