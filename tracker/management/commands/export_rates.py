import csv
from django.core.management.base import BaseCommand
from tracker.models import Currency

class Command(BaseCommand):
    help = 'export rates'

    def handle(self, *args, **options):
        with open('rates_export.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Код', 'Назва', 'Курс'])
            for curr in Currency.objects.filter(is_active=True):
                # Беремо останній запис з історії
                last_rate = curr.rates.order_by('-timestamp').first()
                rate_val = last_rate.rate if last_rate else 'N/A'
                writer.writerow([curr.code, curr.name, rate_val])
        self.stdout.write("Файл rates_export.csv створено успішно.")