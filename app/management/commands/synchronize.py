from django.core.management.base import BaseCommand
from app.models import Blocks
import requests


class Command(BaseCommand):
    def get_blocks(self):
        result = requests.get('https://bcschain.info/api/blocks')
        json_response = result.json()
        for item in json_response:
            block = Blocks.objects.create(hash=item['hash'], height=item['height'],
                                          timestamp=item['timestamp'],
                                          transactionCount=item['transactionCount'],
                                          miner=item['miner'])
            block.save()

    def handle(self, *args, **options):
        self.get_blocks()
